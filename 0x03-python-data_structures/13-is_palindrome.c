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
	listint_t *slow;
	short i = 0, j = 0;

	if (!head || !*head || !(*head)->next)
		return (1);
	slow = *head;
	arr[i++] = slow->n;
	arr[i++] = slow->next->n;
	slow = slow->next;
	while ((slow = slow->next))
		arr[i++] = slow->n;
	while (j != i)
		if (arr[j++] != arr[--i])
			return (0);
	return (1);
}
