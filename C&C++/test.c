#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

node* create_node(int number);
void place_node(node *list, node *n);
void print_list(node *list);
void free_list(node *list);

int main(int argc, char **argv)
{
    // Memory for numbers
    node *list = NULL;

    // For each CLI argument
    for (int i = 1; i < argc; i++)
    {
        // Convert argument to int
        int number = atoi(argv[i]);

        // Allocate node for number
        node *n = create_node(number);
		if (n == NULL) { return 1; }

        // If list is empty
        if (list == NULL)
        {
            list = n;
        }
        // If number belongs at beginning of list
        else if (n->number < list->number)
        {
            n->next = list;
            list = n;
        }
        // If number belongs later in list
        else
        {
            place_node(list, n);
        }
    }

    // Print numbers
    print_list(list);

    // Free memory
    free_list(list);
}

node* create_node(int number)
{
	node *n = malloc(sizeof(node));
	if (n == NULL)
	{
		return NULL;
	}
	n->number = number;
	n->next = NULL;

	return n;
}

void place_node(node *list, node *n)
{
	// Iterate over nodes in list
	for (node *ptr = list; ptr != NULL; ptr = ptr->next)
	{
		// If at end of list
		if (ptr->next == NULL)
		{
			ptr->next = n;
			return;
		}
		// If in middle of list
		if (n->number < ptr->next->number)
		{
			n->next = ptr->next;
			ptr->next = n;
			return;
		}
	}
}

void print_list(node *list)
{
	for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }
}

void free_list(node *list)
{
	node *ptr = list;
    while (ptr != NULL)
    {
        node *tmp = ptr->next;
        free(ptr);
        ptr = tmp;
    }
}
