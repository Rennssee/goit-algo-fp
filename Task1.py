class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def insertion_sort_linked_list(head):
    dummy = ListNode()
    current = head

    while current is not None:
        prev = dummy
        next_node = current.next

        while prev.next is not None and prev.next.value < current.value:
            prev = prev.next

        current.next = prev.next
        prev.next = current

        current = next_node

    return dummy.next


def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next


# Приклад використання:
if __name__ == "__main__":
    # Створення вхідних списків для тестування
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))

    # Реверсування списку
    reversed_list1 = reverse_linked_list(list1)
    print("Реверсований список:")
    while reversed_list1 is not None:
        print(reversed_list1.value, end=" ")
        reversed_list1 = reversed_list1.next
    print()

    # Сортування вставками
    sorted_list2 = insertion_sort_linked_list(list2)
    print("Відсортований список:")
    while sorted_list2 is not None:
        print(sorted_list2.value, end=" ")
        sorted_list2 = sorted_list2.next
    print()

    # Об'єднання відсортованих списків
    merged_list = merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    while merged_list is not None:
        print(merged_list.value, end=" ")
        merged_list = merged_list.next
    print()
