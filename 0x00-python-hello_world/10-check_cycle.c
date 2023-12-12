#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *pace = list;
	listint_t *speed = list;

	if (!list)
		return (0);

	while (pace && speed && speed->next)
	{
		pace = pace->next;
		speed = speed->next->next;
		if (pace == speed)
			return (1);
	}

	return (0);
}
