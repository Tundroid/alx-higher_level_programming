#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print python list object info
 * @p: python object
*/
void print_python_list_info(PyObject *p)
{
	long int i = -1, s = PyList_Size(p);
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", object->allocated);
	while (++i < s)
		printf("Element %ld: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
}
