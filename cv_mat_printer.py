import gdb
import re

class CVMatrixPrinter:
    def __init__(self, val):
        self.rows = int(val["rows"])
        self.cols = int(val["cols"])
        self.data_ptr = val["data"]
        print(self.rows, self.cols, self.data_ptr)

    def matString(self):
        ptr = self.data_ptr
        if ptr.dereference().type.code != gdb.TYPE_CODE_FLT:
            ptr = ptr.reinterpret_cast(gdb.lookup_type("float").pointer())
            print(ptr.dereference())
        rows = [ [] for r in range(self.rows)]
        widths = [0 for c in range(self.cols)]
        for r in range(self.rows):
            for c in range(self.cols):
                s = '{:.14g}'.format(float(ptr.dereference()))
                widths[c] = max(widths[c], len(s)) # for min blank align in pretty print
                rows[r].append(s)
                ptr += 1
        
        return '\n'.join(map(lambda row: '\t' + ''.join(map(lambda c: '{0:{1}}'.format(row[c], widths[c]+1), range(len(row)))), rows))

    def prefixString(self):
        return 'Mat {row}:{col}'.format(row=self.rows, col=self.cols)
    
    def to_string(self):
        return self.prefixString() + "\n" + self.matString()

def register_printer():
    global pretty_printer_dict
    pretty_printer_dict[re.compile('^cv::Mat$')] = lambda val: CVMatrixPrinter(val)
    gdb.pretty_printers.append(lambda val: lookup_function(val))

def lookup_function(val):
    type = val.type
    if type.code == gdb.TYPE_CODE_REF:
        type = type.target()

    type = type.unqualified().strip_typedefs()
    typename = type.tag 
    if typename == None:
        return None
    for function in pretty_printer_dict:
        if function.search(typename):
            return pretty_printer_dict[function](val)
    return None

pretty_printer_dict = {}