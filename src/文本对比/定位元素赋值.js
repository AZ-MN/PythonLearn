function setComponentValues() {
    // 定位文本输入组件（class为text-input的input元素）并输入"单行"
    var textInput = document.querySelectorAll('.text-input');
    var lastTextInput = textInput[textInput.length - 1];
    if (lastTextInput) {
        lastTextInput.value = '单行';
        lastTextInput.dispatchEvent(new Event('input'))
    }

    // 定位数字输入组件（class为number-input的input元素）并输入"666"
    var numberInput = document.querySelectorAll('.number-input');
    var lastNumberInput = numberInput[numberInput.length - 1]
    if (lastNumberInput) {
        lastNumberInput.value = '666';
        lastNumberInput.dispatchEvent(new Event('input'))
    }

    // 定位日期时间组件（class为datetime-input的input元素）并输入"2024-12-12 00:00"
    var datetimeInput = document.querySelectorAll('.datetime-input');
    var lastDatetimeInput = datetimeInput[datetimeInput.length - 1]
    if (lastDatetimeInput) {
        lastDatetimeInput.value = '2024-12-12 00:00';
        lastDatetimeInput.dispatchEvent(new Event('input'))
    }

    // 定位多行输入组件（class为multi-line-input的textarea元素）并输入"多行"
    var multiLineInput = document.querySelectorAll('.multi-line-input');
    var lastMultiLineInput = multiLineInput[multiLineInput.length - 1]
    if (lastMultiLineInput) {
        lastMultiLineInput.value = '多行';
        lastMultiLineInput.dispatchEvent(new Event('input'))
    }

    // 定位开关组件（class为radio-group里value为true的input[type="radio"]元素）并选择true对应的选项
    var switchInput = document.querySelectorAll('.radio-group input[type="radio"][value="TRUE"]');
    var lastSwitchInput = switchInput[switchInput.length - 1]
    if (lastSwitchInput) {
        lastSwitchInput.click();
        lastSwitchInput.dispatchEvent(new Event('change'))
    }
}

// 在控制台中直接调用这个函数即可执行所有组件的赋值操作
setComponentValues();


// 点击确定按钮关闭自定义弹窗
// 定位“确定”按钮（通过添加的特定类名'confirm-button'来定位）
var confirmButton = document.querySelectorAll('.confirm-button');
var lastConfirmButton = confirmButton[confirmButton.length - 1]
if (lastConfirmButton) {
    // 为“确定”按钮添加点击事件监听器
    lastConfirmButton.click();
}


// 使用document.querySelector方法查找具有指定data-component-id的元素
const targetElement = document.querySelector('.x-form-edit-modal-body [data-component-id="b8234177b30bc9bc37d954d5"]');
// 如果找到该元素
if (targetElement) {
    // 抛出一个错误，提示虚拟字段未被隐藏
    throw new Error('虚拟字段未被隐藏');
}
// 如果未找到元素，打印虚拟字段已隐藏
console.info('虚拟字段已隐藏');


try {
    // 使用document.querySelector方法查找数据选择元素
    const targetElement = document.querySelector('.x-lov-input .el-input__inner');
    if (targetElement) {
        // 尝试模拟点击操作
        targetElement.click();
        console.info("打开数据选择弹窗")
    } else {
        console.info('未找到指定元素，无法点击');
    }
} catch (error) {
    console.error('点击元素时发生错误:', error);
}

try {
    // 使用document.querySelector方法查找保存按钮元素
const saveButton = document.querySelector('.x-form-edit-modal-footer [class="el-button el-button--primary"] > span')
    if (saveButton) {
        // 尝试模拟点击操作
        saveButton.click();
        console.info("点击保存按钮")
    } else {
        console.info('未找到指定元素，无法点击');
    }
} catch (error) {
    console.error('点击元素时发生错误:', error);
}