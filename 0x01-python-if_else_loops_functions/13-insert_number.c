#include "lists.h"

/**
* insert_node - inserts node in a sorted linked list
* @head: of linked list
* @number: data for new node
*
* Return: node at index
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *node, *prev = NULL;

	node = malloc(sizeof(listint_t));
	if (!head || !node)
		return (NULL);
	tmp = *head;
	node->n = number;
	if (!*head)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (tmp)
	{
		if (number <= tmp->n)
		{
			node->next = tmp;
			if (prev)
				prev->next = node;
			else
				*head = node;
			return (node);
		}
		else if (!tmp->next)
		{
			return (add_nodeint_end(head, number));
		}
		prev = tmp;
		tmp = tmp->next;
	}
	return (NULL);
}
