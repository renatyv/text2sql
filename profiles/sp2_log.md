---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:26.140874Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-6d9zef5r/log.sqlite
schema: main
---

# "access_log"  (rows=30)

columns:
"session" varchar255: 22 distinct
"user_id" varchar255: "U001"=7, "U002"=4, "0CVKaz"=2, "1QceiB"=2, "1hI43A"=2, "2mmGwD"=2, "3cv4gm"=2, "AAuoEU"=2, "2bGs3i"=1, "2is8PX"=1, "3CEHe1"=1, "3Gv8vO"=1, "690mvB"=1, "6oABhM"=1, "7jjxQX"=1
"action" varchar255: "view"=11, "1CwlSX"=4, "6SN6DD"=4, "3JMO2k"=3, "EFnoNR"=2, "FGkTe9"=2, "KBlKgT"=2, "7Dn99b"=1, "KKTw9P"=1
"stamp" varchar255: "/detail"=7, "/search"=6, "/top"=6, "2016-01-01 18:00:00"=1, "2016-01-02 20:00:00"=1, "2016-01-03 22:00:00"=1, "2016-01-04 23:00:00"=1, "2016-01-05 00:30:00"=1, "2016-01-06 02:30:00"=1, "2016-01-07 03:30:00"=1, "2016-01-08 04:00:00"=1, "2016-01-09 12:00:00"=1, "2016-01-10 13:00:00"=1, "2016-01-11 15:00:00"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| session | eee2b2 | 1cf768 | 1cf768 |
| user_id | U002 | U002 | U002 |
| action | view | view | view |
| stamp | 2016-01-10 13:00:00 | 2016-01-05 00:30:00 | 2016-01-06 02:30:00 |

# "action_log"  (rows=120)

columns:
"session" varchar255: "989004ea"=72, "47db0370"=18, "87b5725f"=18, "9afaf87c"=12
"user_id" varchar255: "U001"=91, "U002"=29
"action" varchar255: "add_cart"=72, "purchase"=30, "favorite"=6, "review"=6, "view"=6
"category" varchar255: "drama"=90, "action"=24, nulls=6
"products" varchar255: "D001"=54, "D001,D002"=18, "D002"=18, "A004"=6, "A005"=6, "A005,A006"=6, "A006"=6, nulls=6
"amount" int: 1000=18, 2000=12, nulls=90
"stamp" varchar255: "2016-11-03 18:00:00"=48, "2016-11-04 12:00:00"=18, "2016-11-03 18:10:00"=12, "2016-11-03 18:01:00"=6, "2016-11-03 18:02:00"=6, "2016-11-03 19:00:00"=6, "2016-11-03 20:00:00"=6, "2016-11-03 20:30:00"=6, "2016-11-04 13:00:00"=6, "2016-11-04 15:00:00"=6

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| session | 9afaf87c | 87b5725f | 989004ea |
| user_id | U002 | U001 | U001 |
| action | purchase | add_cart | add_cart |
| category | drama | action | drama |
| products | D002 | A006 | D001 |
| amount | 1000 | null | null |
| stamp | 2016-11-04 13:00:00 | 2016-11-04 12:00:00 | 2016-11-03 18:00:00 |

# "action_log_with_ip"  (rows=12)

columns:
"session" varchar255: "0CVKaz"=1, "111f2996"=1, "1QceiB"=1, "1cf7678e"=1, "1hI43A"=1, "3efe001c"=1, "47db0370"=1, "5d5b0997"=1, "5eb2e107"=1, "87b5725f"=1, "989004ea"=1, "fe05e1d8"=1
"user_id" varchar255: "U001"=3, "U002"=2, "U003"=2, "U004"=1, "U005"=1, "U006"=1, "U007"=1, "U008"=1
"action" varchar255: "view"=12
"ip" varchar255: "216.58.220.238"=3, "210.154.149.63"=2, "98.139.183.24"=2, "10.0.0.3"=1, "127.0.0.1"=1, "172.16.0.5"=1, "192.0.0.10"=1, "192.168.0.23"=1
"stamp" varchar255: "2016-11-03 18:00:00"=2, "2016-11-03 19:00:00"=2, "2016-11-03 20:00:00"=2, "2016-11-03 21:00:00"=1, "2016-11-04 18:00:00"=1, "2016-11-04 19:00:00"=1, "2016-11-04 20:00:00"=1, "2016-11-04 21:00:00"=1, "2016-11-04 22:00:00"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| session | fe05e1d8 | 5d5b0997 | 47db0370 |
| user_id | U001 | U006 | U002 |
| action | view | view | view |
| ip | 216.58.220.238 | 172.16.0.5 | 98.139.183.24 |
| stamp | 2016-11-04 18:00:00 | 2016-11-04 20:00:00 | 2016-11-03 19:00:00 |

# "activity_log"  (rows=244)

columns:
"stamp" varchar255: iso-date, 21 distinct
"session" varchar255: "87b5725f"=49, "9afaf87c"=33, "111f2996"=28, "8cc03a54"=22, "989004ea"=21, "1cf7678e"=14, "36dd0df7"=14, "0fe39581"=7, "3efe001c"=7, "47db0370"=7, "5d5b0997"=7, "5eb2e107"=7, "cabf98e8"=7, "d45ec190"=7, "eee2bb21"=7, "fe05e1d8"=7
"action" varchar255: "view"=244
"option" varchar255: "page"=93, "detail"=79, "search"=72
"path" varchar255: "/detail"=55, "/search_list"=50, "/search_input"=25, "/detail/"=24, "/search_list/"=22, "/"=16, ""=12, "/complete"=10, "/confirm"=10, "/input"=10, "/search_input/"=10
"search_type" varchar255: ""=164, "Area-L"=22, "Area-S"=14, "Pref"=14, "Area-L-with-Job"=7, "Line"=7, "Pref-with-Job"=7, "Station-with-Job"=7, "Line-with-Job"=2

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2017-01-09 12:25:25 | 2017-01-09 12:18:43 | 2017-01-09 12:22:51 |
| session | 87b5725f | cabf98e8 | 87b5725f |
| action | view | view | view |
| option | page | page | search |
| path | / | /search_input | /search_list |
| search_type |  |  | Station-with-Job |

# "app1_mst_users"  (rows=2)

columns:
"user_id" varchar255
"name" varchar255
"email" varchar255

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| user_id | U001 | U002 |
| name | Sato | Suzuki |
| email | sato@example.com | suzuki@example.com |

# "app2_mst_users"  (rows=2)

columns:
"user_id" varchar255
"name" varchar255
"phone" varchar255

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| user_id | U001 | U002 |
| name | Ito | Tanaka |
| phone | 080-xxxx-xxxx | 070-xxxx-xxxx |

# "dup_action_log"  (rows=11)

columns:
"stamp" varchar255: "2016-11-03 21:00:00"=2, "2016-11-03 18:00:00"=1, "2016-11-03 19:00:00"=1, "2016-11-03 20:00:00"=1, "2016-11-04 18:00:00"=1, "2016-11-04 19:00:00"=1, "2016-11-04 20:00:00"=1, "2016-11-04 21:00:00"=1, "2016-11-04 22:00:00"=1, "2016-11-04 22:00:10"=1
"session" varchar255: "3efe001c"=2, "111f2996"=1, "1cf7678e"=1, "47db0370"=1, "5d5b0997"=1, "5eb2e107"=1, "87b5725f"=1, "989004ea"=1, "eee2bb21"=1, "fe05e1d8"=1
"user_id" varchar255: "U001"=2, "U004"=2, "U008"=2, "U002"=1, "U003"=1, "U005"=1, "U006"=1, "U007"=1
"action" varchar255: "click"=11
"products" varchar255: "A001"=5, "D001"=4, "D002"=2

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2016-11-04 22:00:10 | 2016-11-04 18:00:00 | 2016-11-03 21:00:00 |
| session | 3efe001c | 87b5725f | fe05e1d8 |
| user_id | U008 | U001 | U004 |
| action | click | click | click |
| products | A001 | D001 | D001 |

# "form_error_log"  (rows=8)

columns:
"stamp" varchar255
"session" varchar255
"form" varchar255
"field" varchar255
"error_type" varchar255
"value" varchar255

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| stamp | 2016-12-30 00:56:08 | 2016-12-30 00:56:08 | 2016-12-30 00:56:08 | 2016-12-30 00:56:09 | 2016-12-30 00:56:09 | 2016-12-30 00:56:09 | 2016-12-30 00:56:42 | 2016-12-30 00:57:21 |
| session | 004dc3ef | 004dc3ef | 00700be4 | 01061716 | 02596e8a | 035a1ebb | 01061716 | 004dc3ef |
| form | regist | regist | cart | regist | regist | cart | regist | regist |
| field | email | kana | email | email | kana | tel | kana | zip |
| error_type | require | require | format_error | format_error | require | format_error | not_kana | format_error |
| value |  |  | xxx---.co.jp | xxx@---cojp |  | 03-99999999 | 山田 太郎 | 101- |

# "form_log"  (rows=45)

columns:
"stamp" varchar255: "2016-12-30 00:56:08"=21, "2016-12-30 00:57:04"=3, "2016-12-30 00:57:31"=3, "2016-12-30 00:57:48"=3, "2016-12-30 00:57:56"=3, "2016-12-30 00:58:50"=3, "2016-12-30 00:58:58"=3, "2016-12-30 01:00:06"=3, "2016-12-30 01:00:19"=3
"session" varchar255: "9b5f320f"=15, "b2dbcc54"=12, "46b4c72c"=6, "42532886"=3, "539eb753"=3, "647219c7"=3, "8e9afadc"=3
"action" varchar255: "view"=45
"path" varchar255: "/regist/confirm"=15, "/contact/input"=12, "/contact/confirm"=6, "/regist/input"=6, "/cart/input"=3, "/contact/complete"=3
"status" varchar255: ""=30, "error"=15

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2016-12-30 01:00:19 | 2016-12-30 00:58:58 | 2016-12-30 00:58:58 |
| session | 9b5f320f | b2dbcc54 | b2dbcc54 |
| action | view | view | view |
| path | /regist/confirm | /contact/confirm | /contact/confirm |
| status | error |  |  |

# "invalid_action_log"  (rows=7)

columns:
"stamp" varchar255
"session" varchar255
"user_id" varchar255
"action" varchar255
"category" varchar255
"products" varchar255
"amount" int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 |
|---|---|---|---|---|---|---|---|
| stamp | null | 2016-11-03 18:00:00 | 2016-11-03 18:00:00 | 2016-11-03 18:01:00 | 2016-11-03 18:02:00 | 2016-11-03 18:10:00 | 2016-11-04 13:00:00 |
| session | 1QceiB | 0CVKaz | 0CVKaz | 0CVKaz | 0CVKaz | 0CVKaz | 1QceiB |
| user_id | U002 | U001 | U001 | U001 | U001 | U001 | U002 |
| action | purchase | favorite | view | add_cart | add_cart | purchase | purchase |
| category | action | drama | null | drama | drama | drama | drama |
| products | A005,A006 | D001 | null | D002 | null | D001,D002 | D002 |
| amount | 1000 | null | null | null | null | 2000 | 1000 |

# "mst_categories"  (rows=8)

columns:
"id" int
"name" varchar255
"stamp" varchar255

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 |
| name | ladys_fashion | mens_fashion | book | game | dvd | cooking | food | supplement |
| stamp | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-02-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 |

# "mst_products_20161201"  (rows=6)

columns:
"product_id" varchar255
"name" varchar255
"price" int
"updated_at" varchar255

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| product_id | A001 | A002 | B001 | B002 | C001 | D001 |
| name | AAA | AAB | BBB | BBD | CCA | DAA |
| price | 3000 | 4000 | 5000 | 3000 | 4000 | 5000 |
| updated_at | 2016-11-03 18:00:00 | 2016-11-03 19:00:00 | 2016-11-03 20:00:00 | 2016-11-03 21:00:00 | 2016-11-04 18:00:00 | 2016-11-04 19:00:00 |

# "mst_products_20170101"  (rows=6)

columns:
"product_id" varchar255
"name" varchar255
"price" int
"updated_at" varchar255

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| product_id | A001 | A002 | B002 | C001 | D001 | D002 |
| name | AAA | AAB | BBD | CCA | DAA | DAD |
| price | 3000 | 4000 | 3000 | 5000 | 5000 | 5000 |
| updated_at | 2016-11-03 18:00:00 | 2016-11-03 19:00:00 | 2016-11-03 21:00:00 | 2016-12-04 18:00:00 | 2016-11-04 19:00:00 | 2016-12-04 19:00:00 |

# "mst_users"  (rows=320)

columns:
"user_id" varchar255: 30 distinct
"sex" varchar255: "F"=168, "M"=152
"birth_date" varchar255: iso-date, 30 distinct
"register_date" varchar255: "2016-10-01"=160, "2016-10-02"=77, "2016-10-10"=27, "2016-10-05"=18, "2016-10-15"=9, "2016-10-16"=9, "2016-11-01"=5, "2016-11-03"=3, "2016-10-18"=2, "2016-11-05"=2, "2016-11-10"=2, "2016-11-28"=2, "2016-10-20"=1, "2016-10-25"=1, "2016-11-04"=1, "2016-11-15"=1
"register_device" varchar255: "pc"=136, "app"=96, "sp"=88
"withdraw_date" varchar255: "2016-10-10"=32, nulls=288

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| user_id | U030 | U002 | U026 |
| sex | M | F | M |
| birth_date | 1959-10-07 | 1953-06-12 | 1969-02-21 |
| register_date | 2016-11-28 | 2016-10-01 | 2016-10-02 |
| register_device | sp | sp | sp |
| withdraw_date | null | 2016-10-10 | null |

# "mst_users_with_card_number"  (rows=3)

columns:
"user_id" varchar255
"card_number" varchar255

indexes: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| user_id | U001 | U002 | U003 |
| card_number | 1234-xxxx-xxxx-xxxx | null | 5678-xxxx-xxxx-xxxx |

# "product_sales"  (rows=10)

columns:
"category_name" varchar255
"product_id" varchar255
"sales" int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| category_name | book | book | book | book | cd | cd | cd | dvd | dvd | dvd |
| product_id | B001 | B002 | B003 | B004 | C001 | C002 | C003 | D001 | D002 | D003 |
| sales | 20000 | 15000 | 10000 | 5000 | 30000 | 20000 | 10000 | 50000 | 20000 | 10000 |

# "purchase_log"  (rows=5)

columns:
"purchase_id" int
"user_id" varchar255
"amount" int
"stamp" varchar255

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| purchase_id | 10001 | 10002 | 10003 | 10004 | 10005 |
| user_id | U001 | U001 | U001 | U002 | U002 |
| amount | 200 | 500 | 200 | 800 | 400 |
| stamp | 2017-01-30 10:00:00 | 2017-02-10 10:00:00 | 2017-02-12 10:00:00 | 2017-03-01 10:00:00 | 2017-03-02 10:00:00 |

# "read_log"  (rows=15)

columns:
"stamp" varchar255: "2016-12-29 21:45:47"=6, "2016-12-29 21:45:49"=1, "2016-12-29 21:45:54"=1, "2016-12-29 21:45:56"=1, "2016-12-29 21:45:59"=1, "2016-12-29 21:46:05"=1, "2016-12-29 21:46:08"=1, "2016-12-29 21:46:13"=1, "2016-12-29 21:46:22"=1, "2016-12-29 21:46:25"=1
"session" varchar255: "df6eb25d"=6, "76c67c39"=4, "77d477cc"=2, "08962ace"=1, "a80ded24"=1, "afbd3d09"=1
"action" varchar255: "view"=6, "read-20%"=3, "read-40%"=2, "read-60%"=2, "read-100%"=1, "read-80%"=1
"url" varchar255: "http://www.example.com/article?id=news731"=6, "http://www.example.com/article?id=trend925"=5, "http://www.example.com/article?id=it605"=2, "http://www.example.com/article?id=news341"=1, "http://www.example.com/article?id=trend132"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2016-12-29 21:46:25 | 2016-12-29 21:46:05 | 2016-12-29 21:45:56 |
| session | df6eb25d | df6eb25d | df6eb25d |
| action | read-100% | read-40% | read-20% |
| url | http://www.example.com/article?id=news731 | http://www.example.com/article?id=news731 | http://www.example.com/article?id=news731 |

- Skipped 1 empty table(s): "action_log_with_noise"
