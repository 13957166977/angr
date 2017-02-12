from .plugin import SimStatePlugin

HEAP_LOCATION = 0xc0000000
HEAP_SIZE = 64*4096

class SimStateLibc(SimStatePlugin):
    """
    This state plugin keeps track of various libc stuff:
    """

    #__slots__ = [ 'heap_location', 'max_str_symbolic_bytes' ]

    LOCALE_ARRAY = [ 0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x03, 0x20, 0x02, 0x20, 0x02, 0x20,
                    0x02, 0x20, 0x02, 0x20, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x02, 0x00, 0x02, 0x00, 0x02, 0x00, 0x02, 0x00,
                    0x01, 0x60, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8,
                    0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8, 0x08, 0xd8,
                    0x08, 0xd8, 0x08, 0xd8, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x08, 0xd5, 0x08, 0xd5, 0x08, 0xd5,
                    0x08, 0xd5, 0x08, 0xd5, 0x08, 0xd5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5,
                    0x08, 0xc5, 0x08, 0xc5, 0x08, 0xc5, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0,
                    0x04, 0xc0, 0x08, 0xd6, 0x08, 0xd6, 0x08, 0xd6,
                    0x08, 0xd6, 0x08, 0xd6, 0x08, 0xd6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6,
                    0x08, 0xc6, 0x08, 0xc6, 0x08, 0xc6, 0x04, 0xc0,
                    0x04, 0xc0, 0x04, 0xc0, 0x04, 0xc0, 0x02, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
                  ]

    TOLOWER_LOC_ARRAY = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                            16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,
                            32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,
                            48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,
                            64,
                            'a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z',
                            91,92,93,94,95,96,
                            'a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z',
                            123,124,125,126,127,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    TOUPPER_LOC_ARRAY = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                            16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,
                            32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,
                            48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,
                            64,
                            'A','B','C','D','E','F','G','H','I','J','K','L','M',
                            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                            91,92,93,94,95,96,
                            'A','B','C','D','E','F','G','H','I','J','K','L','M',
                            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                            123,124,125,126,127,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def __init__(self):
        SimStatePlugin.__init__(self)

        # various thresholds
        self.heap_location = HEAP_LOCATION
        self.mmap_base = HEAP_LOCATION + HEAP_SIZE * 2
        self.buf_symbolic_bytes = 60
        self.max_symbolic_strstr = 1
        self.max_symbolic_strchr = 16
        self.max_variable_size = 128
        self.max_str_len = 128
        self.max_buffer_size = 48
        self.max_strtol_len = 10
        self.max_memcpy_size = 4096

        # strtok
        self.strtok_heap = [ ]
        self.simple_strtok = True
        self.strtok_token_size = 1024

        # helpful stuff
        self.strdup_stack = [ ]

        # as per Andrew:
        # the idea is that there's two abi versions, and for one of them, the
        # address passed to libc_start_main isn't actually the address of the
        # function, but the address of a pointer to a struct containing the
        # actual function address and the table of contents address
        self.ppc64_abiv = None

        # It will be initialized in __libc_start_main SimProcedure
        self.ctype_b_loc_table_ptr = None
        self.ctype_tolower_loc_table_ptr = None
        self.ctype_toupper_loc_table_ptr = None

        self._errno_location = None

    def copy(self):
        c = SimStateLibc()
        c.heap_location = self.heap_location
        c.buf_symbolic_bytes = self.buf_symbolic_bytes
        c.max_symbolic_strstr = self.max_symbolic_strstr
        c.max_symbolic_strchr = self.max_symbolic_strchr
        c.max_variable_size = self.max_variable_size
        c.max_str_len = self.max_str_len
        c.max_buffer_size = self.max_buffer_size
        c.max_strtol_len = self.max_strtol_len
        c.max_memcpy_size = self.max_memcpy_size
        c.strtok_heap = self.strtok_heap[:]
        c.simple_strtok = self.simple_strtok
        c.strtok_token_size = self.strtok_token_size
        c.strdup_stack = self.strdup_stack[:]
        c.ppc64_abiv = self.ppc64_abiv
        c.ctype_b_loc_table_ptr = self.ctype_b_loc_table_ptr
        c.ctype_tolower_loc_table_ptr = self.ctype_tolower_loc_table_ptr
        c.ctype_toupper_loc_table_ptr = self.ctype_toupper_loc_table_ptr
        c._errno_location = self._errno_location
        #c.aa = self.aa

        return c

    def _combine(self, others):
        new_heap_location = max(o.heap_location for o in others)
        if self.heap_location != new_heap_location:
            self.heap_location = new_heap_location
            return True
        else:
            return False

    def merge(self, others, merge_conditions, common_ancestor=None):
        return self._combine(others)

    def widen(self, others):
        return self._combine(others)

    def init_state(self):
        if o.ABSTRACT_MEMORY in self.state.options:
            return

        try:
            self.state.memory.permissions(HEAP_LOCATION)
        except SimMemoryError:
            self.state.memory.map_region(HEAP_LOCATION, 4096*64, 3)


SimStatePlugin.register_default('libc', SimStateLibc)

from ..s_errors import SimMemoryError
from .. import s_options as o
