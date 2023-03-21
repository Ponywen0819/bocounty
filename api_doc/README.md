## 驗證API

- [x]  Login
    
    描述：獲得使用者token
    
    - 輸入
        - school_id: str
            
            使用者註冊之學號
            
        - password: str
            
            使用者設定之密碼
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
- [x]  /Register
    
    描述：註冊帳號，並在註冊成功後取得使用者token
    
    - 輸入
        - school_id: str
            
            使用者註冊之學號
            
        - name: str
            
            使用者註冊之名稱
            
        - password: str
            
            使用者註冊之密碼
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
- [x]  /Logoff
    
    描述：使使用者token失效
    
    - 輸入
        
        無需輸入
        
    - 回應
        - status: int
            
            表示API要求的狀態。
            

## 會員資訊操作API

- [x]  getUserInfo
    
    描述：取得使用者資訊
    
    - 輸入
        - id: str
            
            選填，表示查詢的帳號，預設為使用者本身
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - id: str
            
            使用者編號
            
        - name
            
            該使用者的名字
            
        - intro
            
            該使用者的簡介
            
- [x]  checkUserVerify
    
    描述：確認使用者郵件認證狀態
    
    - 輸入
        
        無需輸入
        
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - verify: int
            
            表示認證狀態
            
            | 代碼 | 認證狀態 |
            | --- | --- |
            | 0 | 尚未認證 |
            | 1 | 已完成認證 |
- [ ]  getUserOutlook
    
    描述：取得使用者外觀設定
    
    - 輸入
        - id: str
            
            選填，表示查詢的帳號，預設為使用者本身
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - face: str
            
            臉部表情配件圖片路徑
            
        - hair: str
            
            頭髮配件設定圖片路徑
            
        - clothe: str
            
            服裝圖片路徑
            
        - item: str
            
            配件圖片路徑
            
- [ ]  getUserItem
    
    描述：取得使用者已擁有的物品
    
    - 輸入
        
        不需要輸入
        
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - list: list[obj]
            
            包含持有裝備的資訊
            
            - item_id: str
                
                配件編號
                
            - type: int
                
                配件種類
                
            - photo: str
                
                配件圖片路徑
                
            - name: str
                
                配件名稱
                
- [x]  getUserCoin
    
    描述：取得使用者擁有之硬幣數量
    
    - 輸入
        
        不需要輸入
        
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - num: int
            
            持有多少硬幣
            
- [x]  changeUserInfo
    
    描述：上傳變更後的使用者名稱或簡介
    
    - 輸入
        - name: str
            
            選填，更改後的名字
            
        - intro: str
            
            選填，更改後的自我介紹
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
- [ ]  changeUserOutlook
    
    描述：更改使用者更改後的服裝搭配。
    
    - 輸入
        - head: str
            
            選填，物品編號
            
        - body: str
            
            選填，物品編號
            
        - leg: str
            
            選填，物品編號
            
        - shoes: str
            
            選填，物品編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            

## 物品操作API

- [ ]  getPoolItemList
    
    描述：給定編號取得該抽獎池中的物品
    
    - 輸入
        - ID: str
            
            抽獎池的編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - items: list[int]
            
            存放所有抽獎池內的物品編號
            
- [ ]  drawCards
    
    描述：給定模式與抽獎池編號，給出抽獎結果
    
    - 輸入
        - type
            
            表示抽獎類型 （單抽、十連抽）
            
        - pool
            
            抽卡池編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - list: list[str]
            
            此次收抽獎所獲得的物品圖片路徑
            

## 委託操作API

- [ ]  getOrderList
    
    描述：依條件取得委託列表
    
    - 輸入
        - type: int
            
            取出委託列表的種類
            
            | 代號 | 取出資料 |
            | --- | --- |
            | 0 | 使用者發出之委託 |
            | 1 | 使用者參加之委託 |
            | 2 | 招募委託列表 |
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - order_list: list[obj]
            
            根據要求給出的委託列表
            
            - order_state: int
                
                表示此委託的狀態
                
                | 編號 | 代表 |
                | --- | --- |
                | 0 | 招募中 |
                | 1 | 進行中 |
                | 2 | 已完成 |
            - title: str
                
                此委託的標題
                
            
            ```json
            {
            	"status": 1,  //int
            	"title": "qwe" //str
            }
            ```
            
- [ ]  getOrderInfo
    
    描述：給定編號取得該委託之資料
    
    - 輸入
        - id: str
            
            此委託的編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - order_state: int
            
            表示此委託的狀態
            
            | 編號 | 代表 |
            | --- | --- |
            | 0 | 招募中 |
            | 1 | 進行中 |
            | 2 | 已完成 |
        - title: str
            
            委託的標題
            
        - intro: str
            
            委託的介紹內容
            
        - price: int
            
            委託的酬勞
            
        - time: str
            
            委託的執行時間
            
        - owner: str
            
            委託人的編號
            
- [ ]  pushOrderState
    
    描述：給定編號使該委託進入下一階段
    
    - 輸入
        - id: str
            
            委託之編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - order_state: int
            
            委託現在的狀態
            
            | 編號 | 代表 |
            | --- | --- |
            | 0 | 招募中 |
            | 1 | 進行中 |
            | 2 | 已完成 |
- [ ]  createOrder
    
    描述：創建新的委託
    
    - 輸入
        - title: str
            
            此委託的標題
            
        - close_time: str
            
            此委託的招募期限
            
        - exec_time: str
            
            此委託的執行時間
            
        - price: int
            
            此委託的酬勞
            
        - intro: str
            
            此委託的介紹內容
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - id: str
            
            新委託的編號
            
- [ ]  deleteOrder
    
    描述：刪除委託
    
    - 輸入
        - id: str
            
            欲刪除委託之編號
            
    - 回應
        - status:int
            
            表示API要求的狀態。
            

## 訊息操作API

- [ ]  getChatInfo
    
    描述：給定編號取得該聊天室資訊
    
    - 輸入
        - id: str
            
            聊天室編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - chaters: list[str]
            
            此聊天室參加人的列表
            
        - owner_id: str
            
            聊天室擁有者編號
            
- [ ]  getChatHistory
    
    描述：給定編號取得該聊天室之歷史內容
    
    - 輸入
        - id: str
            
            聊天室編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - message:list[obj]
            
            訊息紀錄
            
            - content: str
                
                訊息內容
                
            - sender_id: str
                
                訊息傳送方編號
                
            - time: str
                
                訊息傳送時間
                
- [ ]  assignOrder
    
    描述：指派委託給聊天室的另一方
    
    - 輸入
        - chat_id: str
    - 回應
        - status: int
            
            表示API要求的狀態。
            
- [ ]  confirmOrder
    
    描述：確認承接人完成委託並且發放獎勵
    
    - 輸入
        - order_id: str
            
            委託的編號
            
        - involver_id: str
            
            承接人編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            

## 管理員API

- [x]  listPool
    
    描述：取出卡池列表
    
    - 輸入
        
        不需要輸入
        
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - pool_list: list[obj]
            
            卡池資料集合
            
            - id: str
                
                卡池編號
                
            - num: int
                
                卡池內容物數量
                
            - name: str
                
                卡池名稱
                
            - photo: str
                
                卡池圖片路徑
                
- [x]  createPool
    
    描述：創建新的抽卡池
    
    - 輸入
        - name: str
            
            卡池名稱
            
        - photo: str
            
            圖片資料，使用base64轉換成字串
            
    - 回應
        - status: int
            
            表示API要求的狀態
            
        - pool_id:
            
            新建卡池編號
            
- [x]  deletePool
    
    描述：刪除抽卡池
    
    - 輸入
        - Id: str
            
            該卡池之編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
- [ ]  modifyPoolItem
    
    描述：變更抽卡池內容
    
    - 輸入
        - id: str
            
            卡池編號
            
        - modify_list: list[str]
            
            更改後的物品編號列表
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
- [x]  listItem
    
    描述：列出系統內發行的道具
    
    - 輸入
        
        無需輸入
        
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - item_list: list[obj]
            
            配件列表
            
            - id: str
                
                此配件的編號
                
            - name: str
                
                此配件的名稱
                
            - photo: str
                
                此配件圖片路徑
                
            - type: int
                
                配件的種類
                
- [x]  createItem
    
    描述：新增物品
    
    - 輸入
        - name: str
            
            此配件的名稱
            
        - type: int
            
            此配件的種類
            
        - photo: str
            
            此配件圖片，使用base64將圖片資料轉換成字串
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        - id: str
            
            新增加道具的編號。
            
- [x]  deleteItem
    
    描述：刪除物品
    
    - 輸入
        - id: str
            
            此配件的編號
            
    - 回應
        - status: int
            
            表示API要求的狀態。
            
        
- [x]  modifyItemInfo
    
    描述：更改配件資訊
    
    - 輸入
        - id: str
            
            更改配件的編號
            
        - name: str
            
            選填，更改後的名稱
            
        - photo: str
            
            選填，更改後的照片資料，以base64編碼
            
        - type: int
            
            選填，更改後的配件類型
            
    - 回應
        - status: int
            
            表示API要求的狀態。