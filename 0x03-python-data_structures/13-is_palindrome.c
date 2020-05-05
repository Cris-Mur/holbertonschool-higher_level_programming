#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_nodeint - add new node
 * @head: input linked list
 * @n: data of the new node
 * Return: updated list
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = n;
	new->next = *head;
	*head = new;
	return (*head);
}


/**
 * is_palindrome - function that check if list is palindrome
 * @head: input linked list
 * Return: 1 as long the list is palindrome (NULL is 1)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL, *l_tmp = NULL, *aux = NULL;
	int ret = 0;

	if (!head || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp->n != tmp->next->n && tmp->next)
	{
		add_nodeint(&l_tmp, tmp->n);
		tmp = tmp->next;
	}
	add_nodeint(&l_tmp, tmp->n);
	tmp = tmp->next;
	aux = l_tmp;
	while (tmp->next && aux->next)
	{
		if (tmp->n == aux->n)
			ret = 1;
		else
		{
			ret = 0;
			break;
		}
		tmp = tmp->next;
		aux = aux->next;
	}
	if (tmp->n == aux->n)
		ret = 1;
	else
	{
		ret = 0;
	}
	free_listint(l_tmp);
	return (ret);
}
