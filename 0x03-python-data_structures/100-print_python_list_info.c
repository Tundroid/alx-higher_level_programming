#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print python list object info
 * @p: python object
*/
void print_python_list_info(PyObject *p)
{
	int i = 0, s = PyList_Size(p);
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", object->allocated);
	while (i < s)
		printf("Element %d: %s\n", i, Py_TYPE(object->ob_item[i++])->tp_name);
}
