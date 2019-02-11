import multiprocessing as mp
import enlighten
import sys
import time
from multiprocessing import Value
from ctypes import c_bool
from multiprocessing import Process, Manager
from collections import defaultdict

from multiprocessing.managers import BaseManager, DictProxy
from collections import defaultdict
import functools

from multiprocessing.managers import BaseManager, DictProxy


class MyManager(BaseManager):
    pass


MyManager.register('defaultdict', defaultdict, DictProxy)
MyManager.register('dict', dict, DictProxy)
MyManager.register('bool', bool, DictProxy)


#manager = Manager()

mgr = MyManager()
mgr.start()

class DeepDict(defaultdict):
    def __call__(self):
        return DeepDict(self.default_factory)


class CallableDict(defaultdict):
    def __call__(self):
        return mgr.defaultdict( bool)


# class CallableDict(dict):
#     def __call__(self):
#         return dict

MyManager.register('defaultdict', defaultdict, DictProxy)
MyManager.register('DeepDict', DeepDict, DictProxy)
MyManager.register('dict', dict, DictProxy)
MyManager.register('CallableDict', CallableDict, DictProxy)


#self.mgr = MyManager()
#self.mgr.start()

class test(object):

    def __init__(self):
        self.output = mp.Queue()
        self.main = list()
        self.num_iter = 10
        self.status_bars_manager =  self._get_status_bars_manager()
        self.terminated = Value(c_bool, False)
        self.manager = Manager()
        self.x = self.manager.list()
        self.mgr = MyManager()
        self.mgr.start()

        #self.multi_d = self.mgr.defaultdict(lambda: self.mgr.defaultdict(dict) )
        self.multi_d = self.mgr.DeepDict( self.mgr.CallableDict() )  


    def _get_status_bars_manager(self):
        config_status_bar = {'stream': sys.stdout,
                  'usecounter': True, 
                  "set_scroll": True,
                  "resize_lock": True
                  }
        enablecounter_status_bar = config_status_bar['usecounter'] and config_status_bar['stream'].isatty()
        return enlighten.Manager(stream=config_status_bar['stream'], enabled=enablecounter_status_bar, set_scroll=config_status_bar['set_scroll'], resize_lock=config_status_bar['resize_lock'])



    def _get_new_status_bar(self, total, desc, unit, counter_format=False):
        #counter_format
        try:
            self.status_bars_manager
        except attributeerror:
            self.status_bars_manager = self._get_status_bars_manager()

        if counter_format:
            counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit, leave=True, counter_format=counter_format)
        else:
            counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit, leave=True)
        return counter

    def add_num(self,n, status_bar_start =False):
        #status_bar_start =status_bar_start if status_bar_start else self._get_new_status_bar(self.num_iter, self.status_bars_manager.term.center("exporter (sum)") , "", counter_format=self.status_bars_manager.term.bold_white_on_green("{fill}{desc}{fill}"))
        status_bar_start.refresh()
        #self.main = list()
        print(self.num_iter)
        print("self.terminated= ", self.terminated.value)

        for _n in xrange(self.num_iter):
            if _n == 5:
                self.terminated.value = True

            if not self.terminated.value:
                self.multi_d[n][_n]
                time.sleep(1)
                print("self.terminated= ", self.terminated.value)

                status_bar_start.update(incr=1)
                self.output.put((n, _n) )
                self.main.append((n, _n))
                self.x.append((n, _n))
        print("self.main=",self.main)
        print("self.multi_d=", self.multi_d)


    def compute(self):
        #manager = Manager()
        #status_bar_start =status_bar_start if status_bar_start else self._get_new_status_bar(self.num_iter, "exporter (sum)", "")
        #processes = [mp.process(target=self.add_num, args=(__n,) ) for __n in range(4)]
        processes = [mp.Process(target=self.add_num, args=(__n,self._get_new_status_bar(self.num_iter, "exporter (sum)", "")) ) for __n in range(4)]
        for p in processes:
            p.start()

        for p in processes:
            p.join()


        self.results = list()
        while True: 
            if self.output.empty():
                break
            else:
                self.results.append(self.output.get() )


        #self.results



t = test()

t.compute()
