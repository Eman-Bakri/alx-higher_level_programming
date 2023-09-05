#include "lists.h"

/**
 * insert_node - A function that inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: when fails - NULL.
 * Otherwise - the address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNod;

	newNod = malloc(sizeof(listint_t));
	if (newNod == NULL)
		return (NULL);
	newNod->n = number;

	if (node == NULL || node->n >= number)
	{
		newNod->next = node;
		*head = newNod;
		return (newNod);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newNod->next = node->next;
	node->next = newNod;

	return (newNod);
}
