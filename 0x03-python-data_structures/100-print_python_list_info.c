#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - function that print python info
 * @p: python object
 * Return: void function
 */
void print_python_list_info(PyObject *p)
{
	int step;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject*)p)->allocated);
	for (step = 0; step < PyList_Size(p); step++)
		printf("Element %d: %s\n", step, Py_TYPE(
			       PyList_GetItem(p, step))->tp_name);
}
