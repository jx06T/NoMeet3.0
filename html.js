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
        this.AllPeopleList = [""]
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
    openMic(name, x = false) {
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
                if (x) {
                    let T5 = document.querySelectorAll(".kssMZb")
                    T5.forEach(e => {
                        e.classList.remove("kssMZb")
                    })
                    let T6 = HTML.OPMic.querySelector(".IYwVEf")
                    T6.classList.remove("HotEze")
                    HTML.OPMic.classList.add("jx06rrr")

                    let T7 = this.GET_ONE(HTML.AllPeopleList[0])
                    let T8 = T7.querySelector(".DYfzY")
                    T8.classList.add("jx06ff")
                    setTimeout(() => {
                        let T9 = document.querySelector(".LvMmxf")
                        T9.classList.add("FTMc0c")

                    }, 500);
                    console.log(T5, T6, T7, T8, T9)
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
            let T6 = this.GET_ONE(HTML.AllPeopleList[0])
            let T7 = T6.querySelector(".DYfzY")
            T7.classList.remove("jx06ff")
        }, 500);
    }
    openCam(name, x = false) {
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
                    let T5 = HTML.OPCam.querySelector(".IYwVEf")
                    T5.classList.remove("HotEze")
                    HTML.OPCam.classList.add("jx06rrr")
                    // let T6 = this.GET_ONE(this.AllPeopleList)
                    let T6 = this.GET_ONE(HTML.AllPeopleList[0])
                    T6.classList.add("jx06ddd")
                    // T6.style.display = "none"
                    console.log(T5, T6)
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
            let T6 = this.GET_ONE(HTML.AllPeopleList[0])
            T6.classList.remove("jx06ddd")
        }, 500);
    }
    GET_ONE(name = "") {
        console.log(name)
        let T1 = document.querySelectorAll(".dkjMxf")
        let T2 = Array.from(T1).find(e => {
            let T3 = e.querySelector(".dwSJ2e")
            console.log(T3)
            return T3.textContent == name
        })
        if (!T2) {
            T2 = Array.from(T1).find(e => {
                let T3 = e.querySelector(".S7urwe")
                console.log(T3)
                return T3 != null
            })
        }
        if (!T2) {
            T2 = T1[0]
        }
        return T2
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
    OPvideo(name, F) {
        let T1 = this.GET_ONE(name)
        if (!T1) {
            T1 = this.GET_ONE()
        }
        let VideoBox = T1.querySelector('.p2hjYe,.TPpRNe')
        if (VideoBox["jx06"]) {
            VideoBox.firstChild.remove()
        }
        const firstChild = VideoBox.firstChild;
        let V = this.getvideo(F)
        if (!V) {
            return
        }
        VideoBox.insertBefore(V, firstChild);
        this.VideoPlayer = VideoBox.firstChild
        try {
            VideoBox.firstChild.play();
        } catch (error) {
            
        }
        VideoBox["jx06"] = true;
        console.log(VideoBox)
    }

    CLvideo(name, F) {
        let T1 = this.GET_ONE(name)
        if (!T1) {
            T1 = this.GET_ONE()
        }
        let VideoBox = T1.querySelector('.p2hjYe,.TPpRNe')
        if (VideoBox["jx06"]) {
            VideoBox.firstChild.remove()
            VideoBox["jx06"] = false
            this.VideoPlayer = null
        }
    }
    PPvideo(name, F) {
        if (this.VideoPlayer) {
            try {
                if (F) {
                    this.VideoPlayer.play()
                } else {
                    this.VideoPlayer.pause()
                }
            } catch (error) {
                
            }
        }
    }
    getvideo(F) {
        const ext = F.split('.').pop()
        if (ext === 'mp4' || ext === 'webm' || ext === 'ogg'||ext === 'mov') {
            const videoElement = document.createElement("video");
            videoElement.setAttribute("controls", "");
            videoElement.setAttribute("autoplay", "");
            videoElement.setAttribute("name", "media");
            videoElement.setAttribute("class", "jx06video");

            const sourceElement = document.createElement("source");
            // sourceElement.setAttribute("src", "https://static.videezy.com/system/resources/previews/000/041/786/original/94.Data-screen.mp4");
            // sourceElement.setAttribute("src", chrome.runtime.getURL("py/video/wdwf.mp4"));
            let src = chrome.runtime.getURL("py/video/" + F)
            if (!src) {
                return null
            }
            sourceElement.setAttribute("src", src);
            sourceElement.setAttribute("type", "video/mp4");
            videoElement.appendChild(sourceElement);
            videoElement.style.position = 'relative';
            videoElement.style.zIndex = 1;
            videoElement.loop = true
            videoElement.controls = false;
            videoElement.autoplay = true;
            return videoElement

        } else {
            const imgElement = document.createElement("img");
            imgElement.setAttribute("src", chrome.runtime.getURL("py/video/" + F));
            imgElement.setAttribute("class", "jx06video");
            return imgElement;
        }
    }
}