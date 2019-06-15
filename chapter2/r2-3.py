"""
Describe a component from a text-editor GUI and the methods that it encapsulates.

Editor: Nano

The history component which encapsulates the following methods.
/* Move h to the string in the history list just before it, and return
 * that string.  If there isn't one, don't move h and return NULL. */

char *get_history_older(filestruct **h)
{
	if ((*h)->prev == NULL)
		return NULL;

	*h = (*h)->prev;

	return (*h)->data;
}

/* Move h to the string in the history list just after it, and return
 * that string.  If there isn't one, don't move h and return NULL. */
char *get_history_newer(filestruct **h)
{
	if ((*h)->next == NULL)
		return NULL;

	*h = (*h)->next;

	return (*h)->data;
}
"""