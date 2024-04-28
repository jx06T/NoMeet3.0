
// ---------------------------------------------------------------------------

function GetAllPeople(option = { force: false }) {
    if (HTML.MeetingDetails.getAttribute("aria-pressed") == 'true' || HTML.chatroomB.getAttribute("aria-pressed") == 'true' || HTML.Activity.getAttribute("aria-pressed") == 'true') {
        FailureCount++
        if (FailureCount > MaxFailureCount || option.force) {
            FailureCount = 0
        } else {
            if (HTML.AllPeopleList) {
                // HTML.AllPeopleList = Array.from(HTML.AllPeople.querySelectorAll(".zWGUib")).map(i => i.innerText)
                return HTML.AllPeopleList
            }
            return [""]
        }
    }
    let T = false
    if (HTML.AllParticipants.getAttribute("aria-pressed") != 'true') {
        HTML.AllParticipants.click()
        T = true
    }
    const AllPeople = document.querySelector('[class="AE8xFb OrqRRb GvcuGe goTdfd"]')
    if (AllPeople) {
        console.log(AllPeople)
        HTML.AllPeople = AllPeople
        var allpeople = Array.from(HTML.AllPeople.querySelectorAll(".zWGUib")).map(i => i.innerText)
    }
    if (T) {
        HTML.AllParticipants.click()
    }
    if (HTML.AllPeople) {
        HTML.AllPeopleList = allpeople
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
function check2(html) {
    let from = html.querySelector('.RgDGVe')
    let msg = html.querySelector('.LpG93b')

    const fromstate = CheckMessenger(from.innerText)
    const msgstate = CheckMsg(msg.innerText, from.innerText)
    console.log(from, msg, fromstate, msgstate)
    switch (fromstate) {
        case 0:
            html.style.display = "block"
            break
        case 1:
            html.style.display = "none"
            return
    }
    switch (msgstate) {
        case 0:
            html.style.display = "block"
            break
        case 1:
            html.style.display = "none"
            return
    }
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
    const raw = JSON.stringify({ people: GetAllPeople(), A_S: HTML.A_S, A_V: HTML.A_V })
    console.log(HTML.A_S)
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
function is_No_Entering() {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };
    fetch("http://127.0.0.1:5000/can_enter", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            console.log(result)
            if (result == "T") {
                let c = 0
                let temp0 = setInterval(() => {
                    c++
                    let t = document.querySelector('[jsname="Qx7uuf"]')
                    // t.click()
                    if (t || c > 9) {
                        if (t) {
                            t.addEventListener("click", () => {
                                location.href = "https://support.google.com/meet/answer/10620582?hl=zh-Hant&ref_topic=14074340&sjid=18168767818580573851-AP";
                            });
                        }
                        clearInterval(temp0)
                    }
                }, 500);
            }
        })
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
const Listencallback2 = (mutationsList, observer) => {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            if (mutation.addedNodes.length == 0) {
                continue
            }
            if (!mutation.addedNodes[0].classList) {
                continue
            }
            if (mutation.addedNodes[0].classList.contains("BQRwGe")) {
                console.log(mutation.addedNodes[0])
                check2(mutation.addedNodes[0])
            }
        }
        else if (mutation.type === 'attributes') {
        }
    }
}
// ------------------------------------------------------------------------------------

const HTML = new _HTML()
window.onload = () => {
    HTML.init()
}
function start() {
    const config = { attributes: true, childList: true, subtree: true };
    const callback = Listencallback
    const observer = new MutationObserver(callback);
    observer.observe(HTML.MsgBoxFather, config);

    const config2 = { attributes: true, childList: true, subtree: true };
    const callback2 = Listencallback2
    const observer2 = new MutationObserver(callback2);
    observer2.observe(HTML.popMsg, config2);

    console.log(HTML)
    const room_code = HTML.GetRoomCode()

    setTimeout(() => {
        HTML.closeAll()
    }, 1000);
    setTimeout(() => {
        HTML.AllPeopleList = GetAllPeople()
        console.log(HTML.AllPeopleList)
    }, 6000);
    setTimeout(() => {
        HTML.AllPeopleList = GetAllPeople()
        console.log(HTML.AllPeopleList)
    }, 7000);

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
                        case "GET1":
                            postST()
                            HTML.closeAll(true)
                            break;
                        case "FUN":
                            HTML[m.FUN]()
                            break;
                        case "SV":
                            if (m.audience == "else") {
                                if (HTML.isBusy) {
                                    setTimeout(() => {
                                        HTML[m.FUN](m.name, true)
                                    }, 1500);
                                } else {
                                    HTML[m.FUN](m.name, true)
                                    HTML.isBusy = true
                                    setTimeout(() => {
                                        HTML.isBusy = false
                                    }, 1500);
                                }
                            }
                            break
                        case "InsertVideo":
                            HTML.video()
                            console.log(56565656556)
                        default:
                            break;
                    }
                });
            })
            .catch(error => console.log('error', error));
    }, 1000);
}

