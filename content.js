console.log("jjjjjjjjjjjjjjjjjjjjjjjjjjjj")

let count = 0

let FailureCount = 0
let MaxFailureCount = 5

let messagesIsent = [
    "Беркем дә, бу беренче сынау хәбәре.",
];
let HiddenMsg = [
    "jx06H",
    "1",
    "3",
    "5",
]
let HiddenPerson = [
    "jx06P"
]

class _HTML {
    constructor() {
        this.waits = {}
    }
    init() {
        let temp = setInterval(() => {
            // const chatroomB = document.querySelector("[aria-label='與所有參與者進行即時通訊']");
            const chatroomB = document.querySelector("[data-panel-id='2']");
            if (chatroomB) {
                this.chatroomB = chatroomB
                this.nextinit()
                clearInterval(temp)
            }
        }, 500);
    }
    nextinit() {
        const RHB = document.querySelector('[data-promo-anchor-id="e7iErc"]');
        this.RHB = RHB
        const MeetingDetails = document.querySelector('[data-panel-id="5"]');
        this.MeetingDetails = MeetingDetails
        const AllParticipants = document.querySelector('[data-panel-id="1"]');
        this.AllParticipants = AllParticipants
        const Activity = document.querySelector('[data-panel-id="10"]');
        this.Activity = Activity
        const quitB = document.querySelector('[class="VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c  jh0Tpd Gt6sbf QQrMi"]');
        this.quitB = quitB
        const RoomCode = document.querySelector("[class='u6vdEc ouH3xe']");
        this.RoomCode = RoomCode

        let T = false
        if (this.chatroomB.getAttribute("aria-pressed") != 'true') {
            this.chatroomB.click()
            T = true
        }

        const sentB = document.querySelector('[class="VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD tWDL4c  WQTuKc"]')
        this.sentB = sentB
        const inputSpace = document.querySelector("#bfTqV")
        this.inputSpace = inputSpace

        const MsgBoxFather = document.querySelector(".z38b6")
        this.MsgBoxFather = MsgBoxFather
        const BigBox = document.querySelector(".hWX4r")
        this.BigBox = BigBox

        if (T) {
            this.chatroomB.click()
        }

        if (this.MsgBoxFather) {
            start()
        } else {
            setTimeout(() => {
                this.nextinit()
            }, 1000);
        }
    }
    quit() {
        this.quitB.click()
    }
    HoldHand() {
        this.RHB.click()
    }
    HoldHandx10() {
        let c = 0
        let temp = setInterval(() => {
            c++
            this.RHB.click()
            if (c>30) {
                clearInterval(temp)
            }
        }, 200);
    }
    GetRoomCode() {
        return this.RoomCode.innerText
    }
    Reload(){
        location.reload();
    }
}

// ---------------------------------------------------------------------------
function GetAllPeople(option={force:false}) {
    if (HTML.MeetingDetails.getAttribute("aria-pressed") == 'true' || HTML.chatroomB.getAttribute("aria-pressed") == 'true' || HTML.Activity.getAttribute("aria-pressed") == 'true') {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
        } else {
            if (HTML.AllPeople) {
                return Array.from(HTML.AllPeople.querySelectorAll(".zWGUib")).map(i => i.innerText)
            }
            return [""]
        }
    }
    let T = false
    if (HTML.AllParticipants.getAttribute("aria-pressed") != 'true') {
        HTML.AllParticipants.click()
        T = true
    }
    if (!HTML.inputSpace || HTML.inputSpace.value != "") {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
            T = true
        } else {
            if (T) {
                HTML.chatroomB.click()
            }
            if (HTML.AllPeople) {
                return Array.from(HTML.AllPeople.querySelectorAll(".zWGUib")).map(i => i.innerText)
            }
            return [""]
        }
    }
    const AllPeople = document.querySelector('[class="AE8xFb OrqRRb GvcuGe goTdfd"]')
    if (AllPeople) {
        HTML.AllPeople = AllPeople
        var allpeople = Array.from(HTML.AllPeople.querySelectorAll(".zWGUib")).map(i => i.innerText)
    }
    if (T) {
        HTML.AllParticipants.click()
    }
    if (HTML.AllPeople) {
        return allpeople
    }
    return [""]
}

function sendAmsg(text, option = { force: false, hide: true }) {
    if (HTML.MeetingDetails.getAttribute("aria-pressed") == 'true' || HTML.AllParticipants.getAttribute("aria-pressed") == 'true' || HTML.Activity.getAttribute("aria-pressed") == 'true') {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
        } else {
            return
        }
    }
    let T = false
    if (HTML.chatroomB.getAttribute("aria-pressed") != 'true') {
        HTML.chatroomB.click()
        T = true
    }
    if (!HTML.inputSpace || HTML.inputSpace.value != "") {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
            T = true
        } else {
            if (T) {
                HTML.chatroomB.click()
            }
            return
        }
    }
    HTML.inputSpace.value = text;

    var inputEvent = new Event("input", {
        bubbles: true,
        cancelable: true
    });
    if (option.hide) {
        messagesIsent.push(text)
    }
    HTML.inputSpace.dispatchEvent(inputEvent);
    HTML.sentB.click()

    if (T) {
        HTML.chatroomB.click()
    }
}

function CheckMessenger(from) {
    if (!from) {
        return 0
    }
    if (HiddenPerson.includes(from)) {
        return 1
    }
    return 0
}
function CheckMsg(Msg, messenger) {
    if (messagesIsent.includes(Msg)) {
        return 1
    }
    let isMatch = HiddenMsg.some(aRule => {
        let regex = new RegExp(aRule);
        return regex.test(Msg);
    });
    console.log(Msg, messenger, isMatch)
    if (isMatch && messenger != "你") {
        return 1
    }
    return 0
}


function check(html) {
    const box = html.parentNode.parentNode
    const from = box.firstChild.firstChild;
    const time = box.firstChild.firstChild.nextSibling;
    const msg = html.firstChild.firstChild.firstChild;
    const msgs = html.parentNode.childNodes;
    console.log(html, box, from, time, msg, msgs)
    const fromstate = CheckMessenger(from.innerText)
    const msgstate = CheckMsg(msg.innerText, from.innerText)
    switch (fromstate) {
        case 0:
            box.style.display = "block"
            break
        case 1:
            box.style.display = "none"
            break
    }
    switch (msgstate) {
        case 0:
            html.style.display = "block"
            break
        case 1:
            html.style.display = "none"
            break
    }
    let RemoveCount = 0
    for (let i = 0; i < msgs.length; i++) {
        const item = msgs[i]
        if (item.style.display == "none") {
            RemoveCount++
        }
        if (msgs.length <= RemoveCount) {
            box.style.display = "none"
        }
    }
}
// ------------------------------------------------------------------------------------
function postST() {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const raw = JSON.stringify({ people: GetAllPeople() })
    // const raw =  JSON.stringify([1,3,4])
    console.log(raw)
    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };
    fetch("http://127.0.0.1:5000/get", requestOptions)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.error(error));
}
// ------------------------------------------------------------------------------------
const Listencallback = (mutationsList, observer) => {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            if (mutation.addedNodes.length == 0) {
                continue
            }
            if (!mutation.addedNodes[0].classList) {
                continue
            }
            // console.log(mutation.addedNodes)
            if (mutation.addedNodes[0].classList.contains("er6Kjc")) {
                check(mutation.addedNodes[0])
            }
        }
        else if (mutation.type === 'attributes') {
        }
    }
}

const HTML = new _HTML()
HTML.init()
function start() {
    const config = { attributes: true, childList: true, subtree: true };
    const callback = Listencallback
    const observer = new MutationObserver(callback);
    console.log(HTML)
    observer.observe(HTML.MsgBoxFather, config);
    const room_code = HTML.GetRoomCode()
    setTimeout(() => {
        GetAllPeople()
    }, 1000);
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };
    setInterval(() => {
        fetch(`http://127.0.0.1:5000?room_code=${room_code}`, requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log(result)
                result.forEach(m => {
                    switch (m.type) {
                        case "Cmsg":
                            sendAmsg(m.msg, { force: m.force == "T", hide: m.hide == "T" })
                            break;
                        case "GET":
                            postST()
                            break;
                        case "FUN":
                            HTML[m.FUN]()
                            break;
                        default:
                            break;
                    }
                });
            })
            .catch(error => console.log('error', error));
    }, 1000);
}

window.addEventListener('keydown', function (event) {
    var key = event.key;
    if (key === '6') {
        console.log('Key 6 is pressed!');
        sendAmsg("欸你很白癡欸" + count)
        // sendAmsg("欸你很白癡欸" + count, { force: true })
        count++
    }
    if (key === '7') {
        console.log(GetAllPeople())
    }
})
