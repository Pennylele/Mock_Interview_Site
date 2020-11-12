function triggerChangeEvent(option) {
    // set selected property
    option.selected = true;

    // raise event on parent <select> element
    if ("createEvent" in document) {
        var evt = document.createEvent("HTMLEvents");
        evt.initEvent("change", false, true);
        option.parentNode.dispatchEvent(evt);
    } else {
        option.parentNode.fireEvent("onchange");
    }
}


(function setup() {
    const sel = document.querySelector('#slct');
    sel.onchange = () => {

        pythonCode = `print(123)
print('abc')


def add(a, b):
    return a + b


add(1, 2)
`;
        rubyCode = `age = 32
multiplier = 10
age * multiplier

total = age * multiplier


puts total


def test(a1 = "Ruby", a2 = "Perl")

end
test "C", "C++"
test
`;
        cppCode = `#include <iostream>
using namespace std;


int main()
{
   cout << "hellocpp";
   return 0;
}
`;

        code = '';
        if (sel.value === 'python') {
            code = pythonCode;
        } else if (sel.value === 'ruby') {
            code = rubyCode;
        } else if (sel.value === 'cpp') {
            code = cppCode;
        } else {
            code = '';
        }

        document.querySelector('#script_text_area').textContent = code;
    };
})();

function runTest() {
    const sel = document.querySelector('#selector').value;
    const optionEl = document.querySelector(sel);
    triggerChangeEvent(optionEl);
}