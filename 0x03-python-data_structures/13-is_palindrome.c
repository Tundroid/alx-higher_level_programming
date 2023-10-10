#include "lists.h"

/**
 * is_palindrome - checks is a linked list is a palindrome
 *
 * @head: of linked list
 * Return: 1 if lis tis palindrome, otherwise, 0
*/
int is_palindrome(listint_t **head)
{
	int arr[2048];
	listint_t *tmp;
	short i = 0, j = 0;

	if (!head || !*head || !(*head)->next)
		return (1);
	tmp = *head;
	arr[i++] = tmp->n;
	arr[i++] = tmp->next->n;
	tmp = tmp->next;
	while ((tmp = tmp->next))
		arr[i++] = tmp->n;
	while (j != --i)
		if (arr[j++] != arr[i])
			return (0);
	return (1);
}
