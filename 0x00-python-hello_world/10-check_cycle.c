#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - test if the list is a cycle
 * @list: input list
 * Return: Always 1 (success)
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *aux = NULL;

	if (head)
	{
		while (head)
		{
			aux = head;
			head = head->next;
			if (aux <= head)
				return (1);
		}
	}
	return (0);
}
