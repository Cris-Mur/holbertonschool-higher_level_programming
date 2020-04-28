#include "lists.h"

/**
 * insert_node - insert new node in a sorted linked list
 * @head: input linked list
 * @number: input data of the new linked list
 * Return: dir of the new node success, null if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *list = *head;
	listint_t *prev = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		if (number < list->n)
		{
			new->next = list;
			list = new;
			*head = list;
			return (new);
		}
		while (list->n < number && list->next != NULL)
			list = list->next;
		while (prev->next != list )
			prev = prev->next;
		if (list->next == NULL)
		{
			list->next = new;
			return (new);
		}
		prev->next = new;
		new->next = list;
	}
	return (new);
}
