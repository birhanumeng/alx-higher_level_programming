#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: single linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	if (list == NULL || list->next == NULL)
		return (0);

	node1 = list->next;
	node2 = list->next->next;

	while (node1 && node2 && node2->next)
	{
		if (node1 == node2)
			return (1);

		node1 = node1->next;
		node2 = node2->next->next;
	}

	return (0);
}
