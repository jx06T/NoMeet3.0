console.log("jjjjjjjjjjjjjjjjjjjjjjjjjjjj")
let count = 0
let AllMessageCount = -1
let All_Message = []

let FailureCount = 0
let MaxFailureCount = 5
let messagesIsent = [
    "Hello, World!",
    "這是一條測試訊息。",
    "Happy coding!",
    "你今天好嗎？",
    "Testing, testing, 1, 2, 3.",
    "測試，測試，1、2、3。",
    "感謝您使用此服務。",
    "Have a great day!",
];
let HiddenMsg = [
    "白癡"
]
let HiddenPerson = [
    "HH",
]

let allE = {}
let CRDMsg = []
function init() {
    const RHB = document.querySelector("[aria-label='舉手 (ctrl + alt + h)']");
    // const RHB = document.querySelector('[data-tooltip-id="c29"]');
    allE.RHB = RHB
    const MeetingDetails = document.querySelector("[aria-label='會議詳細資料']");
    // const MeetingDetails = document.querySelector('[data-tooltip-id="tt-c32"]');
    allE.MeetingDetails = MeetingDetails
    const AllParticipants = document.querySelector("[aria-label='顯示所有參與者']");
    // const AllParticipants = document.querySelector('[data-tooltip-id="tt-c33"]');
    allE.AllParticipants = AllParticipants
    const Activity = document.querySelector("[aria-label='活動']");
    // const Activity = document.querySelector('[data-tooltip-id="tt-c39"]');
    allE.Activity = Activity
    const quitB = document.querySelector("[aria-label='退出通話']");
    // const quitB = document.querySelector('[data-tooltip-id="tt-c31"]');
    allE.quitB = quitB
    const inputB = document.querySelector("[aria-label='與所有參與者進行即時通訊']");
    // const inputB = document.querySelector('[data-tooltip-id="tt-c34"]');
    allE.inputB = inputB

    if (!inputB) {
        return
    }

    let T = false
    if (inputB.getAttribute("aria-pressed") != 'true') {
        inputB.click()
        T = true
    }

    const inputSpace = document.querySelector("#bfTqV")
    const sentB = document.querySelector("[aria-label='傳送訊息'].VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.QDwDD.tWDL4c.Cs0vCd")
    // const sentB = document.querySelector('[data-tooltip-id="tt-c58"]')
    allE.sentB = sentB
    allE.inputSpace = inputSpace
    const MsgBoxFather = document.querySelector(".z38b6")
    allE.MsgBoxFather = MsgBoxFather
    const BigBox = document.querySelector(".hWX4r")
    allE.BigBox = BigBox

    console.log(allE)
    if (T) {
        inputB.click()
    }
    if (!BigBox) {
        return
    }

    const config = { attributes: true, childList: true, subtree: true };
    const callback = Listencallback
    const observer = new MutationObserver(callback);
    observer.observe(MsgBoxFather, config);

    if (Object.keys(allE).every(key => allE[key])) {
        clearInterval(WaitInit)
        console.log("start")

        let mainn = setInterval(() => {
            main()
        }, 5000);

        setTimeout(() => {
            // quit()
            CreateAmsg("欸你很白癡欸" + count, "啊哈")
            // sendAmsg(messagesIsent[count % messagesIsent.length])
        }, 5000);
    }
}
const Listencallback = (mutationsList, observer) => {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            // console.log(mutation, mutation.addedNodes, mutation.addedNodes[0])
            if (mutation.addedNodes.length == 0) {
                continue
            }
            if (!mutation.addedNodes[0].classList) {
                continue
            }
            if (mutation.addedNodes[0].classList.contains("ptNLrf")) {
                checkMsgIsent(mutation.addedNodes[0])
            }
            if (mutation.addedNodes[0].classList.contains("jx06")) {
                CRDMsg.push(mutation.addedNodes[0].innerText.split("\n"))
                // console.log("!!!!!!!!!!!!!!!!")
                console.log(mutation.addedNodes[0].innerText)
            }
        }
        else if (mutation.type === 'attributes') {
        }
    }
}

function sendAmsg(text, option = { force: false }) {
    if (allE.MeetingDetails.getAttribute("aria-pressed") == 'true' || allE.AllParticipants.getAttribute("aria-pressed") == 'true' || allE.Activity.getAttribute("aria-pressed") == 'true') {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
        } else {
            return
        }
    }
    let T = false
    if (allE.inputB.getAttribute("aria-pressed") != 'true') {
        allE.inputB.click()
        T = true
    }
    if (!allE.inputSpace || allE.inputSpace.value != "") {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
            T = true
        } else {
            if (T) {
                allE.inputB.click()
            }
            return
        }
    }
    allE.inputSpace.value = text;

    var inputEvent = new Event("input", {
        bubbles: true,
        cancelable: true
    });
    allE.inputSpace.dispatchEvent(inputEvent);
    allE.sentB.click()

    if (T) {
        allE.inputB.click()
    }

}

function RaiseHand() {
    allE.RHB.click()
}

function checkMsgIsent(HTML) {
    if (!HTML) {
        return
    }
    console.log(HTML)
    if (CRDMsg.length > 0) {
        CRDMsg.forEach((item) => {
            console.log(item)
            let t = ReductionMsg(item[0], item[1], item[2])
            let referenceNode = HTML.lastElementChild
            HTML.insertBefore(t, referenceNode);
            HTML.style.height  = "50px"
            // HTML.appendChild(t)
        })
    }
    CRDMsg = []

    const father = HTML.parentNode
    const fafather = father.parentNode
    let DelCount = 0
    father.childNodes.forEach(aMsg => {
        const MsgState = CheckMsg(aMsg.firstChild.firstChild.innerText)
        switch (MsgState) {
            case 0:
                HTML.style.display = "block"
                // HTML.classList.remove("hide")
                break;
            case 1:
                HTML.style.display = "none"
                DelCount++
                // HTML.classList.add("hide")
                break;
            default:
                break;
        }

        // let t = window.getComputedStyle(HTML).getPropertyValue("display");
        // console.log(aMsg,HTML.style.display,DelCount,t)
    });
    // console.log(DelCount, father.childNodes.length)
    if (DelCount == father.childNodes.length) {
        fafather.style.display = "none"
    } else {
        fafather.style.display = "block"
    }
}

function check(HTML) {
    if (!HTML && All_Message.length == 0) {
        return
    } else if (!HTML) {
        let m = All_Message[AllMessageCount]
        HTML = m.AllMsg[m.AllMsg.length - 1].html
    }
    console.log("!!check")
    const boxex = document.querySelectorAll(".Ss4fHf")
    let box = HTML.parentNode.parentNode
    let index = Array.from(boxex).indexOf(box)

    if (!All_Message[index]) {
        All_Message.push({ html: box, AllMsg: [], index: index })
        AllMessageCount++
    }

    const F0 = box.firstChild.firstChild;
    const F1 = box.firstChild.firstChild.nextSibling;
    if (F1) {
        var time = F1.innerText;
    } else {
        var time = GetNowTime();
    }
    const F = box.firstChild.nextSibling.childNodes;
    var messenger = F0.innerText;
    const state = CheckMessenger(messenger)
    let m = All_Message[index]
    switch (state) {
        case 1:
            box.style.display = "none"
            break
        case 2:
            box.style.display = "block"
            break
    }


    let RemoveCount = 0
    for (let i = 0; i < F.length; i++) {
        item = F[i]
        console.log(item, i)
        if (!m.AllMsg[i]) {
            const state2 = CheckMsg(HTML, messenger)
            switch (state2) {
                case 1:
                    item.style.display = "none"
                    RemoveCount++
                    break;
                case 0:
                    item.style.display = "block"
                    box.style.display = "block"
                    if (m.AllMsg[i - 1]) {
                        if (m.AllMsg[i - 1].addhtml[m.AllMsg[i - 1].addhtml.length - 1].data[0] != messenger) {
                            F[i - 1].innerText += GetTextData(messenger, GetNowTime())
                            console.log("233")
                        }
                    }
            }
            m.AllMsg.push({ addhtml: [], html: item, msg: item.innerText, index: i, state: state2, messenger: messenger, time: time })
        } else {
            switch (m.AllMsg[i].state) {
                case 0:
                    item.style.display = "block"
                    box.style.display = "block"
                    if (m.AllMsg[i - 1]) {
                        if (m.AllMsg[i - 1].addhtml[m.AllMsg[i - 1].addhtml.length - 1].data[0] != messenger) {
                            F[i - 1].innerText += GetTextData(messenger, GetNowTime())
                            console.log("233")
                        }
                    }
                    break
                case 1:
                    item.style.display = "none"
                    RemoveCount++
                    break;
                case 2:
                    if (m.AllMsg[i - 1]) {
                        if (m.AllMsg[i - 1].addhtml[m.AllMsg[i - 1].addhtml.length - 1].data[0] != m.AllMsg[i].messenger) {
                            F[i - 1].innerText += GetTextData(m.AllMsg[i].messenger, GetNowTime())
                            console.log("233")
                        }
                    }
                    item.innerText = m.AllMsg[i].msg
                    box.style.display = "block"
                    item.style.display = "block"
                    if (i == 0) {
                        F0.innerText = m.AllMsg[i].messenger
                    }
                    for (let k = 0; k < m.AllMsg[i].addhtml.length; k++) {
                        if (k > 0) {
                            if (m.AllMsg[i].addhtml[k - 1].data[0] != m.AllMsg[i].addhtml[k].data[0]) {
                                item.innerText += m.AllMsg[i].addhtml[k].e
                            }
                        } else {
                            if (m.AllMsg[i].messenger != m.AllMsg[i].addhtml[k].data[0]) {
                                item.innerText += m.AllMsg[i].addhtml[k].e
                            }
                        }
                        item.innerText += m.AllMsg[i].addhtml[k].text
                    }
                    break
            }
        }
    }

    if (F.length <= RemoveCount) {
        box.style.display = "none"
    }
    console.log(All_Message)
}


function CheckMessenger(messenger) {
    if (HiddenPerson.includes(messenger)) {
        return 1
    }
    return 0
}

function CheckMsg(Msg, messenger) {
    // 0:沒事 1:消失
    if (messagesIsent.includes(Msg)) {
        return 1
    }
    let isMatch = HiddenMsg.some(aRule => {
        let regex = new RegExp(aRule);
        return regex.test(Msg);
    });
    if (isMatch && messenger != "你") {
        return 1
    }
    return 0
}

function quit() {
    allE.quitB.click()
}

function ReductionMsg(messenger, time, Msg) {
    const D1 = document.createElement("div")
    D1.classList.add("jx062B")
    D1.style.order = 0
    D1.style.display = "block"
    let t = `
       <div class="jx062ST"><div class="jx062S">${messenger}</div> <div class="jx062T">${time}</div></div>
       <div class="jx062M">${Msg}</div>
    `
    D1.innerHTML = t
    return (D1)
}

function CreateAmsg(Msg, messenger) {
    const D1 = document.createElement("div")
    D1.classList.add("Ss4fHf")
    D1.classList.add("jx06")
    D1.style.order = 0
    D1.style.display = "block"
    let t = `
    <div>
        <div class="poVWob jx061S">${messenger}</div>
        <div jsname="biJjHb" class="jx061T MuzmKe">${GetNowTime()}</div>
    </div>
    <div class="beTDc">
        <div class="jx061M">
        ${Msg}
        </div>
    </div>
    `
    D1.innerHTML = t

    allE.MsgBoxFather.appendChild(D1)
}


function GetTextData(messenger, time) {
    let text = `\n\n\n${messenger}　${time}`
    return text
}
function GetNowTime() {
    const now = new Date();
    let n = now.toLocaleTimeString('zh-TW')
    var result = n.substring(0, n.indexOf(":", n.indexOf(":") + 1));
    return result
}

let WaitInit = setInterval(() => {
    init()
}, 3000);


function main() {
    // sendAmsg(messagesIsent[count % messagesIsent.length])
    // CreateAmsg("欸你很白癡欸" + count, "啊哈")
    count++
}
window.addEventListener('keydown', function (event) {
    var key = event.key;

    if (key === '6') {
        console.log('Key 6 is pressed!');
        CreateAmsg("欸你很白癡欸" + count, "啊哈")
    }
})