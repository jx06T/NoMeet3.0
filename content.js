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
        is_No_Entering() //確認是否被封鎖
        chrome.storage.local.get("isAuto").then((r) => {
            if (r.isAuto) {
                console.log("sss")
                let c = 0
                let temp0 = setInterval(() => {
                    c++
                    let t = document.querySelector('[jsname="Qx7uuf"]')
                    // t.click()
                    if (t || c > 9) {
                        if (t) {
                            t.click()
                        }
                        chrome.storage.local.set({ "isAuto": false })
                        clearInterval(temp0)
                    }
                }, 500);
            }
            let temp = setInterval(() => {
                // const chatroomB = document.querySelector("[aria-label='與所有參與者進行即時通訊']");
                const chatroomB = document.querySelector("[data-panel-id='2']");
                console.log(chatroomB)
                if (chatroomB) {
                    this.chatroomB = chatroomB
                    this.nextinit()
                    clearInterval(temp)
                }
            }, 500);
        })
    }
    nextinit() {
        const RHB = document.querySelector('[data-promo-anchor-id="e7iErc"]');
        this.RHB = RHB
        const emoji = document.querySelector('[jsname="G0pghc"]');
        this.emoji = emoji
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


        const OPMic = document.querySelector("[class='fswXR']").querySelector(".Uulb3c");
        this.OPMic = OPMic
        const OPMicS = document.querySelector("[class='fswXR']").querySelector('[class="VYBDae-Bz112c-LgbsSe VYBDae-Bz112c-LgbsSe-OWXEXe-SfQLQb-suEOdc hzfTZb  S7Zu8d"]');
        this.OPMicS = OPMicS
        const OPCam = document.querySelector("[class='VlW4Pb']").querySelector(".eaeqqf");
        this.OPCam = OPCam
        const OPCamS = document.querySelector("[class='VlW4Pb']").querySelector('[class="VYBDae-Bz112c-LgbsSe VYBDae-Bz112c-LgbsSe-OWXEXe-SfQLQb-suEOdc hzfTZb  S7Zu8d"]');
        this.OPCamS = OPCamS

        const popMsg = document.querySelector("[class = 'fJsklc nulMpf Didmac sOkDId']")
        this.popMsg = popMsg

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
    FakeQuit() {
        this.quitB.click()
        let temp = setInterval(() => {
            let t = document.querySelector('[class="roSPhc"]')
            if (t) {
                t.textContent = "你已從會議中被移除"
                // t.textContent = "你已被退出這場會議"
                console.log("!!!!!", t)
                clearInterval(temp)
            }
        }, 100);
    }
    HoldHand() {
        this.RHB.click()
        this.RemoveFlash(this.RHB)
    }
    HoldHandx10() {
        let c = 0
        let temp = setInterval(() => {
            c++
            this.HoldHand()
            if (c > 30) {
                clearInterval(temp)
            }
        }, 200);
    }
    RemoveFlash(html) {
        let c = 0
        let temp = setInterval(() => {
            c++
            html.classList.remove("VfPpkd-Bz112c-LgbsSe-OWXEXe-IT5dJd")
            if (c > 30) {
                clearInterval(temp)
            }
        }, 50);
    }
    SendEmoji(id = 8) {
        // console.log(this.emoji)
        let tt = false
        if (this.emoji.getAttribute("aria-pressed") == "false") {
            this.emoji.click()
            // this.RemoveFlash(this.emoji)
            tt = true
        }
        setTimeout(() => {
            let t = document.querySelector('[jsname="me23c"]')
            if (!t) {
                this.emoji.click()
                return
            }
            t = t.childNodes[id].querySelector("button")
            let c = 0
            let temp = setInterval(() => {
                c++
                t.click()
                if (c > 5) {
                    clearInterval(temp)
                }
            }, 300);
            if (tt) {
                this.emoji.click()
            }
        }, 10);
    }
    GetRoomCode() {
        return this.RoomCode.innerText
    }
    reload() {
        chrome.storage.local.set({ "isAuto": true }).then(() => {
            location.reload();
        })
    }
    openMic(name,x=false) {
        console.log(this.OPMic.parentNode.nextSibling.firstChild)
        if (this.OPMic.getAttribute('data-is-muted') == "true") {
            this.OPMic.click()
        }
        this.OPMicS.click()
        let T1 = document.querySelector(".EDp2nc")
        setTimeout(() => {
            let T2 = T1.firstChild.querySelectorAll("[jsname='K4r5Ff']")
            let T3 = Array.from(T2).find(e => {
                // console.log(e.textContent)
                return e.textContent == name
            })
            let T4 = T3.parentNode
            // console.log(T3,T4)
            T4.click()
            setTimeout(() => {
                this.OPMicS.click()
                if(x){
                    let a = document.querySelectorAll(".kssMZb")
                    a.forEach(e=>{
                        e.classList.remove("kssMZb")
                    })
                    document.querySelector(".LvMmxf").classList.add("FTMc0c")
                    let a2 = HTML.OPMic.querySelector(".IYwVEf")
                    a2.classList.remove("HotEze")
                    HTML.OPMic.classList.add("jx06rrr")
                    console.log(a,a2)
                }
            }, 300);
        }, 500);
    }
    closeMic() {
        if (this.OPMic.getAttribute('data-is-muted') == "false") {
            this.OPMic.click()
        }
        this.OPMicS.click()
        let T1 = document.querySelector(".EDp2nc")
        if (!T1) {
            return
        }
        setTimeout(() => {
            let T2 = T1.firstChild.querySelectorAll("[jsname='K4r5Ff']")
            let T4 = T2[0].parentNode
            T4.click()
            setTimeout(() => {
                this.OPMicS.click()
            }, 300);
            let T3 = Array.from(T2).map(e => {
                return e.textContent
            })
            this.A_S = T3
            // console.log(this.A_S)
        }, 500);
    }
    openCam(name,x=false) {
        console.log(this.OPCam.parentNode.nextSibling.firstChild)
        if (this.OPCam.getAttribute('data-is-muted') == "true") {
            this.OPCam.click()
        }
        this.OPCamS.click()
        let T1 = document.querySelector(".bifLQe")
        if (!T1) {
            return
        }
        setTimeout(() => {
            let T2 = T1.querySelectorAll("[jsname='K4r5Ff']")
            let T3 = Array.from(T2).find(e => {
                // console.log(e.textContent)
                return e.textContent == name
            })
            let T4 = T3.parentNode
            // console.log(T3,T4)
            T4.click()
            setTimeout(() => {
                this.OPCamS.click()
                if (x) {
                    document.querySelector(".aGWPv").style.display = "none"
                    let a = HTML.OPCam.querySelector(".IYwVEf")
                    a.classList.remove("HotEze")
                    HTML.OPCam.classList.add("jx06rrr")
                    console.log(a)
                }
            }, 300);
        }, 500);
    }
    closeCam() {
        if (this.OPCam.getAttribute('data-is-muted') == "false") {
            this.OPCam.click()
        }
        this.OPCamS.click()
        let T1 = document.querySelector(".bifLQe")
        setTimeout(() => {
            let T2 = T1.querySelectorAll("[jsname='K4r5Ff']")
            let T4 = T2[0].parentNode
            T4.click()
            setTimeout(() => {
                this.OPCamS.click()
            }, 300);
            let T3 = Array.from(T2).map(e => {
                return e.textContent
            })
            this.A_V = T3
            document.querySelector(".aGWPv").style.display = "block"
            HTML.OPCam.classList.remove("jx06rrr")
        }, 500);
    }
    closeAll(a = false) {
        setTimeout(() => {
            this.closeMic()
        }, 1500);
        setTimeout(() => {
            this.closeCam()
            if (a) {
                postST()
            }
        }, 3000);
    }
}

// ---------------------------------------------------------------------------

function GetAllPeople(option = { force: false }) {
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
        GetAllPeople()
        HTML.closeAll()
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
                                        HTML[m.FUN](m.name,true)
                                    }, 1500);
                                } else {
                                    HTML[m.FUN](m.name,true)
                                    HTML.isBusy = true
                                    setTimeout(() => {
                                        HTML.isBusy = false
                                    }, 1500);
                                }
                            }
                            break
                        case "sound":
                            if (HTML.isBusy) {
                                setTimeout(() => {
                                    HTML.openMic(m.name)
                                }, 1500);
                            } else {
                                HTML.openMic(m.name)
                                HTML.isBusy = true
                                setTimeout(() => {
                                    HTML.isBusy = false
                                }, 1500);
                            }
                            break;
                        case "video":
                            if (HTML.isBusy) {
                                setTimeout(() => {
                                    HTML.openCam(m.name)
                                }, 1500);
                            } else {
                                HTML.openCam(m.name)
                                HTML.isBusy = true
                                setTimeout(() => {
                                    HTML.isBusy = false
                                }, 1500);
                            }
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
        // HTML.closeMic()
        HTML.closeCam()
    }
    if (key === '7') {
        // HTML.openMic("Line 1 (Virtual Audio Cable)")
        HTML.openCam("OBS Virtual Camera")
        // HTML.SendEmoji()
        // console.log(GetAllPeople())
    }
})

