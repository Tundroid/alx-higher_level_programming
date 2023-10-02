#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @h: pointer to head of linked list
 *
 * Return: 1 if cycle exist, otherwise 0
 */

int check_cycle(listint_t *h)
{
	listint_t *tortoise, *hare;

	if (h)
	{
		tortoise = h;
		hare = h->next;
		while (tortoise && hare && hare->next)
		{
			if (hare == tortoise)
				return (1);
			tortoise = tortoise->next;
			hare = hare->next->next;
		}
	}
	return (0);
}
