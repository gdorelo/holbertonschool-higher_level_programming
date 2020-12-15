#include "lists.h"
/**
 * is_palindrome - checks if the list is a palindrome
 * @head: pointer to head of the list
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	int numbers[1024];
	int i = 0, j = 0;
	listint_t *aux;

	if (!head)
		return (0);
	aux = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (; aux; aux = aux->next, i++)
		numbers[i] = aux->n;

	for (; j < i; j++, i--)
	{
		if (numbers[j] != numbers[i - 1])
			return (0);
	}
	return (1);
}
