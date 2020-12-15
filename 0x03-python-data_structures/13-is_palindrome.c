#include "lists.h"
/**
 * is_palindrome - checks if the list is a palindrome
 * @head: pointer to head of the list
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	int arr[1024];
	int i = 0, j = 0;
	listint_t *aux;

	if (!head)
		return (0);
	aux = *head;
	if (!*head || (*head)->next == NULL)
		return (1);
	for (; aux; aux = aux->next, i++)
		arr[i] = aux->n;
	for (; i > j; i--, j++)
	{
		if (arr[i - 1] != arr[j])
			return (0);
	}
	return (1);
}
