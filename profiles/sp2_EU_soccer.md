---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:50.781184Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-sovra9qs/EU_soccer.sqlite
schema: main
---

## Relationships

- League.id ← Match.league_id
- Player.player_api_id ← Match.away_player_1, Match.away_player_10, Match.away_player_11, Match.away_player_2, Match.away_player_3, Match.away_player_4, Match.away_player_5, Match.away_player_6, Match.away_player_7, Match.away_player_8, Match.away_player_9, Match.home_player_1, Match.home_player_10, Match.home_player_11, Match.home_player_2, Match.home_player_3, Match.home_player_4, Match.home_player_5, Match.home_player_6, Match.home_player_7, Match.home_player_8, Match.home_player_9, Player_Attributes.player_api_id
- Player.player_fifa_api_id ← Player_Attributes.player_fifa_api_id
- Team.team_api_id ← Match.away_team_api_id, Match.home_team_api_id, Team_Attributes.team_api_id
- Team.team_fifa_api_id ← Team_Attributes.team_fifa_api_id
- country.id ← League.country_id, Match.country_id

# Country

```sql
CREATE TABLE `Country` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT UNIQUE
);
```

## Rows

- total=11

| column | latest | sample | sample |
|---|---|---|---|
| id | 24558 | 1 | 21518 |
| name | Switzerland | Belgium | Spain |

## Columns

- id: unique identifier, int 1..24558
- name: unique identifier


# League

```sql
CREATE TABLE `League` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`country_id`	INTEGER,
	`name`	TEXT UNIQUE,
	FOREIGN KEY(`country_id`) REFERENCES `country`(`id`)
);
```

## Rows

- total=11

| column | latest | sample | sample |
|---|---|---|---|
| id | 24558 | 13274 | 17642 |
| country_id | 24558 | 13274 | 17642 |
| name | Switzerland Super League | Netherlands Eredivisie | Portugal Liga ZON Sagres |

## Columns

- id: unique identifier, int 1..24558
- country_id: unique identifier, int 1..24558
- name: unique identifier


# Match

```sql
CREATE TABLE `Match` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`country_id`	INTEGER,
	`league_id`	INTEGER,
	`season`	TEXT,
	`stage`	INTEGER,
	`date`	TEXT,
	`match_api_id`	INTEGER UNIQUE,
	`home_team_api_id`	INTEGER,
	`away_team_api_id`	INTEGER,
	`home_team_goal`	INTEGER,
	`away_team_goal`	INTEGER,
	`home_player_X1`	INTEGER,
	`home_player_X2`	INTEGER,
	`home_player_X3`	INTEGER,
	`home_player_X4`	INTEGER,
	`home_player_X5`	INTEGER,
	`home_player_X6`	INTEGER,
	`home_player_X7`	INTEGER,
	`home_player_X8`	INTEGER,
	`home_player_X9`	INTEGER,
	`home_player_X10`	INTEGER,
	`home_player_X11`	INTEGER,
	`away_player_X1`	INTEGER,
	`away_player_X2`	INTEGER,
	`away_player_X3`	INTEGER,
	`away_player_X4`	INTEGER,
	`away_player_X5`	INTEGER,
	`away_player_X6`	INTEGER,
	`away_player_X7`	INTEGER,
	`away_player_X8`	INTEGER,
	`away_player_X9`	INTEGER,
	`away_player_X10`	INTEGER,
	`away_player_X11`	INTEGER,
	`home_player_Y1`	INTEGER,
	`home_player_Y2`	INTEGER,
	`home_player_Y3`	INTEGER,
	`home_player_Y4`	INTEGER,
	`home_player_Y5`	INTEGER,
	`home_player_Y6`	INTEGER,
	`home_player_Y7`	INTEGER,
	`home_player_Y8`	INTEGER,
	`home_player_Y9`	INTEGER,
	`home_player_Y10`	INTEGER,
	`home_player_Y11`	INTEGER,
	`away_player_Y1`	INTEGER,
	`away_player_Y2`	INTEGER,
	`away_player_Y3`	INTEGER,
	`away_player_Y4`	INTEGER,
	`away_player_Y5`	INTEGER,
	`away_player_Y6`	INTEGER,
	`away_player_Y7`	INTEGER,
	`away_player_Y8`	INTEGER,
	`away_player_Y9`	INTEGER,
	`away_player_Y10`	INTEGER,
	`away_player_Y11`	INTEGER,
	`home_player_1`	INTEGER,
	`home_player_2`	INTEGER,
	`home_player_3`	INTEGER,
	`home_player_4`	INTEGER,
	`home_player_5`	INTEGER,
	`home_player_6`	INTEGER,
	`home_player_7`	INTEGER,
	`home_player_8`	INTEGER,
	`home_player_9`	INTEGER,
	`home_player_10`	INTEGER,
	`home_player_11`	INTEGER,
	`away_player_1`	INTEGER,
	`away_player_2`	INTEGER,
	`away_player_3`	INTEGER,
	`away_player_4`	INTEGER,
	`away_player_5`	INTEGER,
	`away_player_6`	INTEGER,
	`away_player_7`	INTEGER,
	`away_player_8`	INTEGER,
	`away_player_9`	INTEGER,
	`away_player_10`	INTEGER,
	`away_player_11`	INTEGER,
	`goal`	TEXT,
	`shoton`	TEXT,
	`shotoff`	TEXT,
	`foulcommit`	TEXT,
	`card`	TEXT,
	`cross`	TEXT,
	`corner`	TEXT,
	`possession`	TEXT,
	`B365H`	NUMERIC,
	`B365D`	NUMERIC,
	`B365A`	NUMERIC,
	`BWH`	NUMERIC,
	`BWD`	NUMERIC,
	`BWA`	NUMERIC,
	`IWH`	NUMERIC,
	`IWD`	NUMERIC,
	`IWA`	NUMERIC,
	`LBH`	NUMERIC,
	`LBD`	NUMERIC,
	`LBA`	NUMERIC,
	`PSH`	NUMERIC,
	`PSD`	NUMERIC,
	`PSA`	NUMERIC,
	`WHH`	NUMERIC,
	`WHD`	NUMERIC,
	`WHA`	NUMERIC,
	`SJH`	NUMERIC,
	`SJD`	NUMERIC,
	`SJA`	NUMERIC,
	`VCH`	NUMERIC,
	`VCD`	NUMERIC,
	`VCA`	NUMERIC,
	`GBH`	NUMERIC,
	`GBD`	NUMERIC,
	`GBA`	NUMERIC,
	`BSH`	NUMERIC,
	`BSD`	NUMERIC,
	`BSA`	NUMERIC,
	FOREIGN KEY(`country_id`) REFERENCES `country`(`id`),
	FOREIGN KEY(`league_id`) REFERENCES `League`(`id`),
	FOREIGN KEY(`home_team_api_id`) REFERENCES `Team`(`team_api_id`),
	FOREIGN KEY(`away_team_api_id`) REFERENCES `Team`(`team_api_id`),
	FOREIGN KEY(`home_player_1`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_2`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_3`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_4`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_5`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_6`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_7`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_8`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_9`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_10`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`home_player_11`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_1`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_2`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_3`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_4`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_5`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_6`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_7`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_8`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_9`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_10`) REFERENCES `Player`(`player_api_id`),
	FOREIGN KEY(`away_player_11`) REFERENCES `Player`(`player_api_id`)
);
```

## Rows

- total=25979

| column | latest | sample | sample |
|---|---|---|---|
| id | 25979 | 15837 | 11099 |
| country_id | 24558 | 15722 | 10257 |
| league_id | 24558 | 15722 | 10257 |
| season | 2015/2016 | 2008/2009 | 2010/2011 |
| stage | 9 | 22 | 17 |
| date | 2015-09-23 00:00:00 | 2009-04-03 00:00:00 | 2010-12-19 00:00:00 |
| match_api_id | 1992095 | 506695 | 888322 |
| home_team_api_id | 10192 | 8569 | 9976 |
| away_team_api_id | 9931 | 8025 | 8540 |
| home_team_goal | 4 | 2 | 1 |
| away_team_goal | 3 | 1 | 1 |
| home_player_X1 | 1 | null | 1 |
| home_player_X2 | 2 | null | 2 |
| home_player_X3 | 4 | null | 4 |
| home_player_X4 | 6 | null | 6 |
| home_player_X5 | 8 | null | 8 |
| home_player_X6 | 2 | null | 2 |
| home_player_X7 | 4 | null | 4 |
| home_player_X8 | 6 | null | 6 |
| home_player_X9 | 8 | null | 8 |
| home_player_X10 | 4 | null | 4 |
| home_player_X11 | 6 | null | 6 |
| away_player_X1 | 1 | null | 1 |
| away_player_X2 | 2 | null | 2 |
| away_player_X3 | 4 | null | 4 |
| away_player_X4 | 6 | null | 6 |
| away_player_X5 | 8 | null | 8 |
| away_player_X6 | 4 | null | 3 |
| away_player_X7 | 6 | null | 5 |
| away_player_X8 | 3 | null | 7 |
| away_player_X9 | 5 | null | 4 |
| away_player_X10 | 7 | null | 6 |
| away_player_X11 | 5 | null | 5 |
| home_player_Y1 | 1 | null | 1 |
| home_player_Y2 | 3 | null | 3 |
| home_player_Y3 | 3 | null | 3 |
| home_player_Y4 | 3 | null | 3 |
| home_player_Y5 | 3 | null | 3 |
| home_player_Y6 | 7 | null | 7 |
| home_player_Y7 | 7 | null | 7 |
| home_player_Y8 | 7 | null | 7 |
| home_player_Y9 | 7 | null | 7 |
| home_player_Y10 | 10 | null | 10 |
| home_player_Y11 | 10 | null | 10 |
| away_player_Y1 | 1 | null | 1 |
| away_player_Y2 | 3 | null | 3 |
| away_player_Y3 | 3 | null | 3 |
| away_player_Y4 | 3 | null | 3 |
| away_player_Y5 | 3 | null | 3 |
| away_player_Y6 | 6 | null | 6 |
| away_player_Y7 | 6 | null | 6 |
| away_player_Y8 | 8 | null | 6 |
| away_player_Y9 | 8 | null | 8 |
| away_player_Y10 | 8 | null | 8 |
| away_player_Y11 | 11 | null | 11 |
| home_player_1 | 274787 | null | 42692 |
| home_player_2 | 492132 | null | 41879 |
| home_player_3 | 108451 | 68744 | 27733 |
| home_player_4 | 25815 | null | 41809 |
| home_player_5 | 94553 | null | 24493 |
| home_player_6 | 384376 | null | 38060 |
| home_player_7 | 598355 | null | 39194 |
| home_player_8 | 36785 | 2625 | 41816 |
| home_player_9 | 45174 | 68773 | 30548 |
| home_player_10 | 302079 | 92222 | 39496 |
| home_player_11 | 71764 | null | 25338 |
| away_player_1 | 156175 | 93450 | 27659 |
| away_player_2 | 95216 | null | 39422 |
| away_player_3 | 172768 | 13437 | 39419 |
| away_player_4 | 22834 | 23930 | 40855 |
| away_player_5 | 458806 | 13554 | 24622 |
| away_player_6 | 207234 | null | 39207 |
| away_player_7 | 25772 | 69417 | 107502 |
| away_player_8 | 40274 | 30975 | 39367 |
| away_player_9 | 34035 | null | 147951 |
| away_player_10 | 41726 | null | 129391 |
| away_player_11 | 527103 | null | 32747 |
| goal | null | null | <goal><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><elapsed_plus>2</elapsed_plus><event_incident_typefk>288</event_incident_typefk><elapsed>45</elapsed><subtype>deflected</subtype><player1>147951</player1><sortorder>4</sortorder><team>8540</team><id>1337584</id><n>197</n><type>goal</type><goal_type>n</goal_type></value><value><comment>p</comment><stats><penalties>1</penalties></stats><event_incident_typefk>20</event_incident_typefk><elapsed>54</elapsed><player1>41879</player1><sortorder>0</sortorder><team>9976</team><id>1337710</id><n>203</n><type>goal</type><goal_type>p</goal_type></value></goal> |
| shoton | null | null | <shoton><value><stats><shoton>1</shoton></stats><event_incident_typefk>135</event_incident_typefk><elapsed>30</elapsed><subtype>shot</subtype><player1>39496</player1><sortorder>0</sortorder><team>9976</team><n>183</n><type>shoton</type><id>1337382</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>553</event_incident_typefk><elapsed>35</elapsed><subtype>big chance shot</subtype><player1>147951</player1><sortorder>0</sortorder><team>8540</team><n>188</n><type>shoton</type><id>1337439</id></value><value><stats><blocked>1</blocked></stats><event_incident_typefk>61</event_incident_typefk><elapsed>43</elapsed><subtype>blocked_shot</subtype><player1>32747</player1><sortorder>0</sortorder><team>8540</team><n>194</n><type>shoton</type><id>1337540</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>312</event_incident_typefk><elapsed>56</elapsed><subtype>deflected</subtype><player1>30284</player1><sortorder>0</sortorder><team>8540</team><n>204</n><type>shoton</type><id>1337726</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>147</event_incident_typefk><elapsed>57</elapsed><subtype>shot</subtype><player1>39422</player1><sortorder>0</sortorder><team>8540</team><n>207</n><type>shoton</type><id>1337743</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>135</event_incident_typefk><elapsed>57</elapsed><subtype>shot</subtype><player1>107502</player1><sortorder>2</sortorder><team>8540</team><n>206</n><type>shoton</type><id>1337751</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>135</event_incident_typefk><elapsed>69</elapsed><subtype>shot</subtype><player1>39367</player1><sortorder>0</sortorder><team>8540</team><n>218</n><type>shoton</type><id>1337857</id></value><value><stats><blocked>1</blocked></stats><event_incident_typefk>494</event_incident_typefk><elapsed>74</elapsed><subtype>blocked_shot</subtype><player1>41879</player1><sortorder>0</sortorder><team>9976</team><n>221</n><type>shoton</type><id>1337900</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>153</event_incident_typefk><elapsed>75</elapsed><subtype>shot</subtype><player1>155254</player1><sortorder>0</sortorder><team>9976</team><n>222</n><type>shoton</type><id>1337917</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>135</event_incident_typefk><elapsed>77</elapsed><subtype>shot</subtype><player1>147951</player1><sortorder>2</sortorder><team>8540</team><n>224</n><type>shoton</type><id>1337933</id></value><value><stats><blocked>1</blocked></stats><event_incident_typefk>61</event_incident_typefk><elapsed>81</elapsed><subtype>blocked_shot</subtype><player1>147951</player1><sortorder>1</sortorder><team>8540</team><n>229</n><type>shoton</type><id>1337990</id></value></shoton> |
| shotoff | null | null | <shotoff><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>9</event_incident_typefk><elapsed>6</elapsed><subtype>distance</subtype><player1>129391</player1><sortorder>0</sortorder><team>8540</team><n>167</n><type>shotoff</type><id>1337197</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>81</event_incident_typefk><elapsed>18</elapsed><subtype>direct_freekick</subtype><player1>32747</player1><sortorder>0</sortorder><team>8540</team><n>173</n><type>shotoff</type><id>1337278</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>21</elapsed><subtype>shot</subtype><player1>38060</player1><sortorder>0</sortorder><team>9976</team><n>178</n><type>shotoff</type><id>1337305</id></value><value><stats><shotoff>1</shotoff></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>53</event_incident_typefk><elapsed>45</elapsed><subtype>volley</subtype><player1>129391</player1><sortorder>0</sortorder><team>8540</team><n>195</n><type>shotoff</type><id>1337561</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>53</event_incident_typefk><elapsed>64</elapsed><subtype>volley</subtype><player1>147951</player1><sortorder>2</sortorder><team>8540</team><n>212</n><type>shotoff</type><id>1337814</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>317</event_incident_typefk><elapsed>66</elapsed><subtype>deflected</subtype><player1>39422</player1><sortorder>2</sortorder><team>8540</team><n>214</n><type>shotoff</type><id>1337833</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>68</elapsed><subtype>shot</subtype><player1>129391</player1><sortorder>1</sortorder><team>8540</team><n>217</n><type>shotoff</type><id>1337848</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>71</elapsed><subtype>shot</subtype><player1>39367</player1><sortorder>0</sortorder><team>8540</team><n>219</n><type>shotoff</type><id>1337880</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>47</event_incident_typefk><elapsed>79</elapsed><subtype>header</subtype><player1>39207</player1><sortorder>1</sortorder><team>8540</team><n>227</n><type>shotoff</type><id>1337957</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>80</elapsed><subtype>shot</subtype><player1>30284</player1><sortorder>0</sortorder><team>8540</team><n>228</n><type>shotoff</type><id>1337971</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>82</elapsed><subtype>shot</subtype><player1>147951</player1><sortorder>0</sortorder><team>8540</team><n>230</n><type>shotoff</type><id>1337994</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>83</elapsed><subtype>shot</subtype><player1>197514</player1><sortorder>0</sortorder><team>8540</team><n>233</n><type>shotoff</type><id>1338010</id></value><value><stats><shotoff>1</shotoff></stats><elapsed_plus>3</elapsed_plus><event_incident_typefk>587</event_incident_typefk><elapsed>90</elapsed><subtype>big chance shot</subtype><player1>30284</player1><sortorder>2</sortorder><team>8540</team><n>238</n><type>shotoff</type><id>1338132</id></value></shotoff> |
| foulcommit | null | null | <foulcommit><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>3</elapsed><player1>107502</player1><sortorder>0</sortorder><team>8540</team><n>164</n><type>foulcommit</type><id>1337169</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>4</elapsed><player2>39367</player2><player1>41816</player1><sortorder>0</sortorder><team>9976</team><n>165</n><type>foulcommit</type><id>1337176</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>5</event_incident_typefk><elapsed>13</elapsed><player2>41809</player2><subtype>serious_foul</subtype><player1>147951</player1><sortorder>0</sortorder><team>8540</team><n>170</n><type>foulcommit</type><id>1337251</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>17</elapsed><player2>32747</player2><player1>25338</player1><sortorder>0</sortorder><team>9976</team><n>172</n><type>foulcommit</type><id>1337273</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>24</elapsed><player2>39367</player2><player1>38060</player1><sortorder>1</sortorder><team>9976</team><n>182</n><type>foulcommit</type><id>1337340</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>26</elapsed><player2>38060</player2><player1>39419</player1><sortorder>0</sortorder><team>8540</team><n>180</n><type>foulcommit</type><id>1337348</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>19</event_incident_typefk><elapsed>30</elapsed><player2>27733</player2><subtype>from_behind</subtype><player1>39207</player1><sortorder>1</sortorder><team>8540</team><n>185</n><type>foulcommit</type><id>1337387</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>5</event_incident_typefk><elapsed>33</elapsed><player2>39367</player2><subtype>serious_foul</subtype><player1>25338</player1><sortorder>0</sortorder><team>9976</team><n>191</n><type>foulcommit</type><id>1337412</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>48</elapsed><player2>147951</player2><player1>39496</player1><sortorder>0</sortorder><team>9976</team><n>199</n><type>foulcommit</type><id>1337657</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>118</event_incident_typefk><elapsed>53</elapsed><player2>30548</player2><subtype>penalty</subtype><player1>40855</player1><sortorder>0</sortorder><team>8540</team><n>201</n><type>foulcommit</type><id>1337702</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>58</elapsed><player2>155254</player2><player1>40855</player1><sortorder>2</sortorder><team>8540</team><n>210</n><type>foulcommit</type><id>1337761</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>73</elapsed><player1>107502</player1><sortorder>1</sortorder><team>8540</team><n>220</n><type>foulcommit</type><id>1337897</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>82</elapsed><player2>39207</player2><player1>155254</player1><sortorder>3</sortorder><team>9976</team><n>232</n><type>foulcommit</type><id>1338003</id></value><value><stats><foulscommitted>1</foulscommitted></stats><elapsed_plus>2</elapsed_plus><event_incident_typefk>37</event_incident_typefk><elapsed>90</elapsed><player2>27723</player2><player1>30284</player1><sortorder>0</sortorder><team>8540</team><n>235</n><type>foulcommit</type><id>1338112</id></value><value><stats><foulscommitted>1</foulscommitted></stats><elapsed_plus>3</elapsed_plus><event_incident_typefk>37</event_incident_typefk><elapsed>90</elapsed><player2>197514</player2><player1>24493</player1><sortorder>0</sortorder><team>9976</team><n>236</n><type>foulcommit</type><id>1338125</id></value></foulcommit> |
| card | null | null | <card><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>203</event_incident_typefk><elapsed>17</elapsed><card_type>y</card_type><subtype>emergency_brake</subtype><player1>25338</player1><sortorder>1</sortorder><team>9976</team><n>174</n><type>card</type><id>1337275</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>203</event_incident_typefk><elapsed>26</elapsed><card_type>y</card_type><subtype>emergency_brake</subtype><player1>39419</player1><sortorder>1</sortorder><team>8540</team><n>179</n><type>card</type><id>1337351</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>70</event_incident_typefk><elapsed>30</elapsed><card_type>y</card_type><player1>39207</player1><sortorder>2</sortorder><team>8540</team><n>184</n><type>card</type><id>1337391</id></value><value><comment>y2</comment><stats><rcards>1</rcards></stats><event_incident_typefk>177</event_incident_typefk><elapsed>33</elapsed><card_type>y2</card_type><subtype>serious_fouls</subtype><player1>25338</player1><sortorder>1</sortorder><team>9976</team><n>187</n><type>card</type><id>1337423</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>73</event_incident_typefk><elapsed>53</elapsed><card_type>y</card_type><subtype>serious_fouls</subtype><player1>40855</player1><sortorder>1</sortorder><team>8540</team><n>202</n><type>card</type><id>1337704</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><elapsed_plus>3</elapsed_plus><event_incident_typefk>70</event_incident_typefk><elapsed>90</elapsed><card_type>y</card_type><player1>24493</player1><sortorder>5</sortorder><team>9976</team><n>239</n><type>card</type><id>1339667</id></value></card> |
| cross | null | null | <cross><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>5</elapsed><subtype>cross</subtype><player1>38060</player1><sortorder>1</sortorder><team>9976</team><n>168</n><type>cross</type><id>1337191</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>20</elapsed><subtype>cross</subtype><player1>41879</player1><sortorder>3</sortorder><team>9976</team><n>176</n><type>cross</type><id>1337298</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>20</elapsed><subtype>cross</subtype><player1>30548</player1><sortorder>5</sortorder><team>9976</team><n>177</n><type>corner</type><id>1337304</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>29</elapsed><subtype>cross</subtype><player1>147951</player1><sortorder>0</sortorder><team>8540</team><n>181</n><type>cross</type><id>1337376</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>32</elapsed><subtype>cross</subtype><player1>30548</player1><sortorder>0</sortorder><team>9976</team><n>189</n><type>cross</type><id>1337405</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>36</elapsed><subtype>cross</subtype><player1>147951</player1><sortorder>0</sortorder><team>8540</team><n>190</n><type>cross</type><id>1337458</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>38</elapsed><subtype>cross</subtype><player1>30548</player1><sortorder>1</sortorder><team>9976</team><n>192</n><type>cross</type><id>1337485</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>40</elapsed><subtype>cross</subtype><player1>147951</player1><sortorder>1</sortorder><team>8540</team><n>193</n><type>cross</type><id>1337503</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>2</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>45</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>2</sortorder><team>8540</team><n>196</n><type>cross</type><id>1337581</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>47</elapsed><subtype>cross</subtype><player1>30284</player1><sortorder>0</sortorder><team>8540</team><n>198</n><type>corner</type><id>1337654</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>52</elapsed><subtype>cross</subtype><player1>30548</player1><sortorder>1</sortorder><team>9976</team><n>200</n><type>corner</type><id>1337687</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>56</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>1</sortorder><team>8540</team><n>205</n><type>cross</type><id>1337735</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>57</elapsed><subtype>cross</subtype><player1>30284</player1><sortorder>1</sortorder><team>8540</team><n>208</n><type>corner</type><id>1337747</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>58</elapsed><subtype>cross</subtype><player1>39422</player1><sortorder>0</sortorder><team>8540</team><n>209</n><type>cross</type><id>1337756</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>64</elapsed><subtype>cross</subtype><player1>30284</player1><sortorder>1</sortorder><team>8540</team><n>211</n><type>cross</type><id>1337812</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>66</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>0</sortorder><team>8540</team><n>213</n><type>cross</type><id>1337828</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>327</event_incident_typefk><elapsed>67</elapsed><subtype>cross</subtype><sortorder>0</sortorder><team>8540</team><n>215</n><type>corner</type><id>1337834</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>77</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>0</sortorder><team>8540</team><n>223</n><type>cross</type><id>1337929</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>79</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>0</sortorder><team>8540</team><n>226</n><type>corner</type><id>1337950</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>82</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>2</sortorder><team>8540</team><n>231</n><type>cross</type><id>1337997</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>85</elapsed><subtype>cross</subtype><player1>147951</player1><sortorder>0</sortorder><team>8540</team><n>234</n><type>cross</type><id>1338034</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>3</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>90</elapsed><subtype>cross</subtype><player1>39422</player1><sortorder>1</sortorder><team>8540</team><n>237</n><type>cross</type><id>1338129</id></value></cross> |
| corner | null | null | <corner><value><stats><corners>1</corners></stats><event_incident_typefk>330</event_incident_typefk><elapsed>20</elapsed><subtype>short</subtype><player1>38060</player1><sortorder>2</sortorder><team>9976</team><n>186</n><type>corner</type><id>1337297</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>20</elapsed><subtype>cross</subtype><player1>30548</player1><sortorder>5</sortorder><team>9976</team><n>177</n><type>corner</type><id>1337304</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>47</elapsed><subtype>cross</subtype><player1>30284</player1><sortorder>0</sortorder><team>8540</team><n>198</n><type>corner</type><id>1337654</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>52</elapsed><subtype>cross</subtype><player1>30548</player1><sortorder>1</sortorder><team>9976</team><n>200</n><type>corner</type><id>1337687</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>57</elapsed><subtype>cross</subtype><player1>30284</player1><sortorder>1</sortorder><team>8540</team><n>208</n><type>corner</type><id>1337747</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>327</event_incident_typefk><elapsed>67</elapsed><subtype>cross</subtype><sortorder>0</sortorder><team>8540</team><n>215</n><type>corner</type><id>1337834</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>79</elapsed><subtype>cross</subtype><player1>24622</player1><sortorder>0</sortorder><team>8540</team><n>226</n><type>corner</type><id>1337950</id></value></corner> |
| possession | null | null | <possession><value><comment>36</comment><event_incident_typefk>352</event_incident_typefk><elapsed>24</elapsed><subtype>possession</subtype><sortorder>0</sortorder><awaypos>64</awaypos><homepos>36</homepos><n>30</n><type>special</type><id>1337336</id></value><value><comment>41</comment><elapsed_plus>2</elapsed_plus><event_incident_typefk>352</event_incident_typefk><elapsed>45</elapsed><subtype>possession</subtype><sortorder>9</sortorder><awaypos>59</awaypos><homepos>41</homepos><n>69</n><type>special</type><id>1337598</id></value><value><comment>40</comment><event_incident_typefk>352</event_incident_typefk><elapsed>68</elapsed><subtype>possession</subtype><sortorder>0</sortorder><awaypos>60</awaypos><homepos>40</homepos><n>143</n><type>special</type><id>1337847</id></value><value><comment>40</comment><elapsed_plus>4</elapsed_plus><event_incident_typefk>352</event_incident_typefk><elapsed>90</elapsed><subtype>possession</subtype><sortorder>1</sortorder><awaypos>60</awaypos><homepos>40</homepos><n>126</n><type>special</type><id>1338167</id></value></possession> |
| B365H | null | null | 3.5000000000 |
| B365D | null | null | 3.1000000000 |
| B365A | null | null | 2.2000000000 |
| BWH | null | null | 3.4000000000 |
| BWD | null | null | 3.2000000000 |
| BWA | null | null | 2.1000000000 |
| IWH | null | null | 3.2000000000 |
| IWD | null | null | 3.2000000000 |
| IWA | null | null | 2.1000000000 |
| LBH | null | null | 3.4000000000 |
| LBD | null | null | 3.2000000000 |
| LBA | null | null | 2.1000000000 |
| PSH | null | null | null |
| PSD | null | null | null |
| PSA | null | null | null |
| WHH | null | null | 3.3000000000 |
| WHD | null | null | 3.3000000000 |
| WHA | null | null | 2.2000000000 |
| SJH | null | null | 3.5000000000 |
| SJD | null | null | 3.2000000000 |
| SJA | null | null | 2.1500000000 |
| VCH | null | null | 3.6000000000 |
| VCD | null | null | 3.2500000000 |
| VCA | null | null | 2.2500000000 |
| GBH | null | null | 3.3000000000 |
| GBD | null | null | 3.2000000000 |
| GBA | null | null | 2.1500000000 |
| BSH | null | null | 3.2500000000 |
| BSD | null | null | 3.2000000000 |
| BSA | null | null | 2.2000000000 |

## Columns

- id: unique identifier, int 1..25979
- country_id: 1729=3040, 4769=3040, 21518=3040, 10257=3017, 7809=2448, 13274=2448, 17642=2052, 15722=1920, 19694=1824, 1=1728, 24558=1422, int 1..24558
- league_id: 1729=3040, 4769=3040, 21518=3040, 10257=3017, 7809=2448, 13274=2448, 17642=2052, 15722=1920, 19694=1824, 1=1728, 24558=1422, int 1..24558
- season: "2008/2009"=3326, "2015/2016"=3326, "2014/2015"=3325, "2010/2011"=3260, "2012/2013"=3260, "2009/2010"=3230, "2011/2012"=3220, "2013/2014"=3032
- stage: 38 distinct, int 1..38
  - stats: average=18.2428, median=18
- date: 1694 distinct
- match_api_id: unique identifier, int 483129..2216672
- home_team_api_id: 299 distinct, int 1601..274581
- away_team_api_id: 299 distinct, int 1601..274581
- home_team_goal: 1=8400, 2=6339, 0=5896, 3=3288, 4=1385, 5=457, 6=161, 7=38, 8=9, 9=4, 10=2, int 0..10
- away_team_goal: 1=8989, 0=8687, 2=5146, 3=2145, 4=718, 5=215, 6=63, 7=10, 8=5, 9=1, int 0..9
- home_player_X1: 1=24146, 0=11, 2=1, nulls=1821, int 0..2
- home_player_X2: 2=22229, 3=1414, 1=258, 4=188, 6=31, 8=19, 0=11, 5=6, 7=2, nulls=1821, int 0..8
- home_player_X3: 4=22575, 5=920, 6=274, 3=257, 8=70, 2=33, 7=17, 1=1, nulls=1832, int 1..8
- home_player_X4: 6=21967, 7=1409, 8=313, 5=264, 2=93, 4=92, 3=9, nulls=1832, int 2..8
- home_player_X5: 8=22056, 1=796, 2=690, 7=253, 6=175, 4=120, 5=27, 3=24, 9=6, nulls=1832, int 1..9
- home_player_X6: 4=7549, 2=7245, 3=6034, 5=1960, 1=932, 9=255, 6=121, 7=37, 8=14, nulls=1832, int 1..9
- home_player_X7: 4=8073, 6=7526, 5=5998, 3=1543, 2=796, 7=161, 8=41, 9=7, 1=2, nulls=1832, int 1..9
- home_player_X8: 6=8069, 3=6302, 7=5991, 5=1603, 8=828, 4=747, 2=584, 9=17, 1=6, nulls=1832, int 1..9
- home_player_X9: 8=7757, 5=7686, 3=4738, 7=1524, 4=826, 9=809, 6=756, 2=45, 1=6, nulls=1832, int 1..9
- home_player_X10: 4=9696, 7=6357, 5=5522, 9=921, 6=874, 8=682, 3=76, 1=10, 2=9, nulls=1832, int 1..9
- home_player_X11: 6=9796, 5=9571, 7=4654, 4=65, 3=59, 1=2, nulls=1832, int 1..7
- away_player_X1: 1=24144, 2=2, 6=1, nulls=1832, int 1..6
- away_player_X2: 2=22109, 3=1469, 1=329, 4=175, 6=28, 8=28, 5=7, 7=2, nulls=1832, int 1..8
- away_player_X3: 4=22465, 5=967, 3=331, 6=271, 8=65, 2=34, 7=13, 9=1, nulls=1832, int 2..9
- away_player_X4: 6=21856, 7=1468, 5=331, 8=325, 2=88, 4=69, 3=7, 1=3, nulls=1832, int 1..8
- away_player_X5: 8=21915, 1=837, 2=695, 7=321, 6=175, 4=152, 3=21, 5=19, 9=12, nulls=1832, int 1..9
- away_player_X6: 4=7564, 2=6865, 3=6038, 5=1978, 1=1214, 9=322, 6=117, 7=37, 8=12, nulls=1832, int 1..9
- away_player_X7: 4=7637, 6=7530, 5=6022, 3=1868, 2=914, 7=137, 8=35, 1=3, 9=1, nulls=1832, int 1..9
- away_player_X8: 6=7621, 3=6268, 7=6007, 5=1894, 4=905, 8=858, 2=574, 9=17, 1=3, nulls=1832, int 1..9
- away_player_X9: 5=7525, 8=7350, 3=4749, 7=1823, 6=929, 4=879, 9=847, 2=39, 1=5, nulls=1833, int 1..9
- away_player_X10: 4=9193, 7=6332, 5=5544, 9=1206, 6=921, 8=840, 3=97, 2=8, 1=5, nulls=1833, int 1..9
- away_player_X11: 5=10043, 6=9322, 7=4664, 4=61, 3=49, 8=1, nulls=1839, int 3..8
- home_player_Y1: 1=24146, 0=11, 3=1, nulls=1821, int 0..3
- home_player_Y2: 3=24147, 0=11, nulls=1821
- home_player_Y3: 3=24146, 5=1, nulls=1832
- home_player_Y4: 3=24142, 5=5, nulls=1832
- home_player_Y5: 3=22691, 7=1403, 5=45, 6=7, 8=1, nulls=1832, int 3..8
- home_player_Y6: 7=14027, 6=7967, 5=1793, 3=288, 8=69, 9=3, nulls=1832, int 3..9
- home_player_Y7: 7=15634, 6=7016, 5=795, 8=694, 9=5, 3=3, nulls=1832, int 3..9
- home_player_Y8: 7=15943, 8=7194, 6=519, 5=463, 9=21, 3=6, 10=1, nulls=1832, int 3..10
- home_player_Y9: 7=10024, 8=8041, 10=4772, 9=1247, 6=62, 1=1, nulls=1832, int 1..10
- home_player_Y10: 10=13568, 8=7083, 9=1516, 7=1188, 11=711, 6=80, 3=1, nulls=1832, int 3..11
- home_player_Y11: 10=13567, 11=10577, 1=2, 3=1, nulls=1832, int 1..11
- away_player_Y1: 1=24144, 3=3, nulls=1832
- away_player_Y2: 3=24147, nulls=1832
- away_player_Y3: 3=24146, 7=1, nulls=1832
- away_player_Y4: 3=24145, 5=1, 7=1, nulls=1832, int 3..7
- away_player_Y5: 3=22645, 7=1448, 5=38, 6=15, 9=1, nulls=1832, int 3..9
- away_player_Y6: 7=13954, 6=8054, 5=1715, 3=350, 8=70, 9=3, 10=1, nulls=1832, int 3..10
- away_player_Y7: 7=15607, 6=7037, 8=772, 5=725, 3=3, 9=2, 10=1, nulls=1832, int 3..10
- away_player_Y8: 7=15903, 8=7265, 6=541, 5=412, 9=22, 10=3, 3=1, nulls=1832, int 3..10
- away_player_Y9: 7=10043, 8=8057, 10=4767, 9=1199, 6=78, 5=1, 11=1, nulls=1833, int 5..11
- away_player_Y10: 10=13145, 8=7173, 7=1575, 9=1518, 11=655, 6=80, nulls=1833, int 6..11
- away_player_Y11: 10=13145, 11=10993, 7=1, 8=1, nulls=1839, int 7..11
- home_player_1: 906 distinct, nulls=1224, int 2984..698273
  - stats: average=76638.4, median=38230
- home_player_2: 2414 distinct, nulls=1315, int 2802..748432
  - stats: average=106854, median=42388
- home_player_3: 2375 distinct, nulls=1281, int 2752..705484
  - stats: average=91601.3, median=39731
- home_player_4: 2606 distinct, nulls=1323, int 2752..723037
  - stats: average=94540.2, median=41060
- home_player_5: 2769 distinct, nulls=1316, int 2752..733787
  - stats: average=109528, median=45996
- home_player_6: 3798 distinct, nulls=1325, int 2625..750584
  - stats: average=102309, median=41467
- home_player_7: 3422 distinct, nulls=1227, int 2625..692984
  - stats: average=97287.6, median=41432
- home_player_8: 4076 distinct, nulls=1309, int 2625..693171
  - stats: average=107291, median=43319
- home_player_9: 4114 distinct, nulls=1273, int 2625..730065
  - stats: average=111132, median=45605
- home_player_10: 3642 distinct, nulls=1436, int 2625..742405
  - stats: average=105613, median=43296
- home_player_11: 2890 distinct, nulls=1555, int 2802..726956
  - stats: average=103414, median=42091
- away_player_1: 926 distinct, nulls=1234, int 2796..698273
  - stats: average=76628.2, median=38289
- away_player_2: 2504 distinct, nulls=1278, int 2790..748432
  - stats: average=107615, median=42388
- away_player_3: 2470 distinct, nulls=1293, int 2752..705484
  - stats: average=91126.8, median=39892
- away_player_4: 2657 distinct, nulls=1321, int 2752..728414
  - stats: average=95083.9, median=41083
- away_player_5: 2884 distinct, nulls=1335, int 2790..746419
  - stats: average=109801, median=46212
- away_player_6: 3930 distinct, nulls=1313, int 2625..722766
  - stats: average=102308, median=41634.5
- away_player_7: 3620 distinct, nulls=1235, int 2625..750435
  - stats: average=97898.1, median=41433
- away_player_8: 4249 distinct, nulls=1341, int 2625..717248
  - stats: average=109265, median=45816
- away_player_9: 4319 distinct, nulls=1328, int 2625..722766
  - stats: average=111087, median=45860
- away_player_10: 3891 distinct, nulls=1441, int 2770..722766
  - stats: average=107149, median=45358
- away_player_11: 3040 distinct, nulls=1554, int 2802..726956
  - stats: average=104933, median=42652
- goal: 13225 distinct, nulls=11762
- shoton: 8464 distinct, nulls=11762
- shotoff: 8464 distinct, nulls=11762
- foulcommit: 8466 distinct, nulls=11762
- card: 13777 distinct, nulls=11762
- cross: 8466 distinct, nulls=11762
- corner: 8465 distinct, nulls=11762
- possession: 8420 distinct, nulls=11762
- B365H: 121 distinct, nulls=3387, num 1.0400000000..26.0000000000
  - stats: average=2.62882, median=2.1
- B365D: 72 distinct, nulls=3387, num 1.4000000000..17.0000000000
  - stats: average=3.83968, median=3.5
- B365A: 115 distinct, nulls=3387, num 1.0800000000..51.0000000000
  - stats: average=4.66222, median=3.5
- BWH: 237 distinct, nulls=3404, num 1.0300000000..34.0000000000
  - stats: average=2.55924, median=2.1
- BWD: 133 distinct, nulls=3404, num 1.6500000000..19.5000000000
  - stats: average=3.7476, median=3.4
- BWA: 261 distinct, nulls=3404, num 1.1000000000..51.0000000000
  - stats: average=4.39695, median=3.4
- IWH: 147 distinct, nulls=3459, num 1.0300000000..20.0000000000
  - stats: average=2.46761, median=2.1
- IWD: 73 distinct, nulls=3459, num 1.5000000000..11.0000000000
  - stats: average=3.60893, median=3.3
- IWA: 159 distinct, nulls=3459, num 1.1000000000..25.0000000000
  - stats: average=4.15058, median=3.3
- LBH: 129 distinct, nulls=3423, num 1.0400000000..26.0000000000
  - stats: average=2.5362, median=2.1
- LBD: 72 distinct, nulls=3423, num 1.4000000000..19.0000000000
  - stats: average=3.71174, median=3.4
- LBA: 128 distinct, nulls=3423, num 1.1000000000..51.0000000000
  - stats: average=4.38535, median=3.3
- PSH: 948 distinct, nulls=14811, num 1.0400000000..36.0000000000
  - stats: average=2.81645, median=2.2
- PSD: 665 distinct, nulls=14811, num 2.2000000000..29.0000000000
  - stats: average=4.13232, median=3.64
- PSA: 1475 distinct, nulls=14811, num 1.0900000000..47.5000000000
  - stats: average=4.97274, median=3.61
- WHH: 125 distinct, nulls=3408, num 1.0200000000..26.0000000000
  - stats: average=2.57874, median=2.15
- WHD: 78 distinct, nulls=3408, num 1.0200000000..17.0000000000
  - stats: average=3.6653, median=3.3
- WHA: 136 distinct, nulls=3408, num 1.0800000000..51.0000000000
  - stats: average=4.48259, median=3.4
- SJH: 137 distinct, nulls=8882, num 1.0400000000..23.0000000000
  - stats: average=2.56606, median=2.1
- SJD: 79 distinct, nulls=8882, num 1.4000000000..15.0000000000
  - stats: average=3.75588, median=3.4
- SJA: 132 distinct, nulls=8882, num 1.1000000000..41.0000000000
  - stats: average=4.62234, median=3.5
- VCH: 160 distinct, nulls=3411, num 1.0300000000..36.0000000000
  - stats: average=2.66811, median=2.15
- VCD: 82 distinct, nulls=3411, num 1.6200000000..26.0000000000
  - stats: average=3.89905, median=3.5
- VCA: 151 distinct, nulls=3411, num 1.0800000000..67.0000000000
  - stats: average=4.84028, median=3.5
- GBH: 159 distinct, nulls=11817, num 1.0500000000..21.0000000000
  - stats: average=2.49876, median=2.1
- GBD: 84 distinct, nulls=11817, num 1.4500000000..11.0000000000
  - stats: average=3.64819, median=3.3
- GBA: 172 distinct, nulls=11817, num 1.1200000000..34.0000000000
  - stats: average=4.3531, median=3.4
- BSH: 101 distinct, nulls=11818, num 1.0400000000..17.0000000000
  - stats: average=2.49789, median=2.1
- BSD: 59 distinct, nulls=11818, num 1.3300000000..13.0000000000
  - stats: average=3.66074, median=3.4
- BSA: 96 distinct, nulls=11818, num 1.1200000000..34.0000000000
  - stats: average=4.40566, median=3.4


# Player

```sql
CREATE TABLE `Player` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`player_api_id`	INTEGER UNIQUE,
	`player_name`	TEXT,
	`player_fifa_api_id`	INTEGER UNIQUE,
	`birthday`	TEXT,
	`height`	INTEGER,
	`weight`	INTEGER
);
```

## Rows

- total=11060

| column | latest | sample | sample |
|---|---|---|---|
| id | 11075 | 3838 | 8237 |
| player_api_id | 39902 | 553557 | 190030 |
| player_name | Zvjezdan Misimovic | Gideon Jung | Pablo Andres Gonzalez |
| player_fifa_api_id | 102359 | 223751 | 198863 |
| birthday | 1982-06-05 00:00:00 | 1994-09-12 00:00:00 | 1985-05-28 00:00:00 |
| height | 180.34 | 187.96 | 180.34 |
| weight | 176 | 168 | 161 |

## Columns

- id: unique identifier, int 1..11075
- player_api_id: unique identifier, int 2625..750584
- player_name: 10848 distinct
- player_fifa_api_id: unique identifier, int 2..234141
- birthday: 5762 distinct
- height: 20 distinct, int 157.48..208.28
  - stats: average=181.867, median=182.88
- weight: 50 distinct, int 117..243
  - stats: average=168.38, median=168


# Player_Attributes

```sql
CREATE TABLE "Player_Attributes" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`player_fifa_api_id`	INTEGER,
	`player_api_id`	INTEGER,
	`date`	TEXT,
	`overall_rating`	INTEGER,
	`potential`	INTEGER,
	`preferred_foot`	TEXT,
	`attacking_work_rate`	TEXT,
	`defensive_work_rate`	TEXT,
	`crossing`	INTEGER,
	`finishing`	INTEGER,
	`heading_accuracy`	INTEGER,
	`short_passing`	INTEGER,
	`volleys`	INTEGER,
	`dribbling`	INTEGER,
	`curve`	INTEGER,
	`free_kick_accuracy`	INTEGER,
	`long_passing`	INTEGER,
	`ball_control`	INTEGER,
	`acceleration`	INTEGER,
	`sprint_speed`	INTEGER,
	`agility`	INTEGER,
	`reactions`	INTEGER,
	`balance`	INTEGER,
	`shot_power`	INTEGER,
	`jumping`	INTEGER,
	`stamina`	INTEGER,
	`strength`	INTEGER,
	`long_shots`	INTEGER,
	`aggression`	INTEGER,
	`interceptions`	INTEGER,
	`positioning`	INTEGER,
	`vision`	INTEGER,
	`penalties`	INTEGER,
	`marking`	INTEGER,
	`standing_tackle`	INTEGER,
	`sliding_tackle`	INTEGER,
	`gk_diving`	INTEGER,
	`gk_handling`	INTEGER,
	`gk_kicking`	INTEGER,
	`gk_positioning`	INTEGER,
	`gk_reflexes`	INTEGER,
	FOREIGN KEY(`player_fifa_api_id`) REFERENCES `Player`(`player_fifa_api_id`),
	FOREIGN KEY(`player_api_id`) REFERENCES `Player`(`player_api_id`)
);
```

## Rows

- total=183978

| column | latest | sample | sample |
|---|---|---|---|
| id | 183978 | 9120 | 4568 |
| player_fifa_api_id | 102359 | 199914 | 144050 |
| player_api_id | 39902 | 188652 | 35831 |
| date | 2007-02-22 00:00:00 | 2010-08-30 00:00:00 | 2014-01-03 00:00:00 |
| overall_rating | 80 | 67 | 72 |
| potential | 81 | 79 | 72 |
| preferred_foot | right | right | right |
| attacking_work_rate | medium | medium | medium |
| defensive_work_rate | low | medium | medium |
| crossing | 74 | 60 | 49 |
| finishing | 68 | 61 | 76 |
| heading_accuracy | 57 | 64 | 67 |
| short_passing | 88 | 76 | 65 |
| volleys | 77 | 56 | 73 |
| dribbling | 87 | 67 | 72 |
| curve | 86 | 59 | 56 |
| free_kick_accuracy | 53 | 57 | 57 |
| long_passing | 78 | 71 | 43 |
| ball_control | 91 | 64 | 74 |
| acceleration | 58 | 74 | 68 |
| sprint_speed | 64 | 75 | 72 |
| agility | 77 | 62 | 70 |
| reactions | 66 | 66 | 75 |
| balance | 73 | 63 | 82 |
| shot_power | 72 | 68 | 76 |
| jumping | 58 | 59 | 80 |
| stamina | 67 | 73 | 54 |
| strength | 59 | 64 | 68 |
| long_shots | 78 | 68 | 58 |
| aggression | 63 | 67 | 56 |
| interceptions | 63 | 61 | 38 |
| positioning | 68 | 60 | 71 |
| vision | 88 | 60 | 57 |
| penalties | 53 | 64 | 68 |
| marking | 38 | 63 | 25 |
| standing_tackle | 32 | 59 | 25 |
| sliding_tackle | 30 | 58 | 21 |
| gk_diving | 9 | 13 | 8 |
| gk_handling | 9 | 13 | 9 |
| gk_kicking | 78 | 5 | 14 |
| gk_positioning | 7 | 5 | 9 |
| gk_reflexes | 15 | 8 | 14 |

## Columns

- id: unique identifier, int 1..183978
- player_fifa_api_id: int 2..234141
- player_api_id: int 2625..750584
- date: profile metrics skipped
- overall_rating: nulls=836, int 33..94
  - stats: average=68.6
- potential: nulls=836, int 39..97
  - stats: average=73.4604
- preferred_foot: nulls=836
- attacking_work_rate: nulls=3230
- defensive_work_rate: nulls=836
- crossing: nulls=836, int 1..95
  - stats: average=55.0869
- finishing: nulls=836, int 1..97
  - stats: average=49.9211
- heading_accuracy: nulls=836, int 1..98
  - stats: average=57.266
- short_passing: nulls=836, int 3..97
  - stats: average=62.4297
- volleys: nulls=2713, int 1..93
  - stats: average=49.4684
- dribbling: nulls=836, int 1..97
  - stats: average=59.1752
- curve: nulls=2713, int 2..94
  - stats: average=52.9657
- free_kick_accuracy: nulls=836, int 1..97
  - stats: average=49.381
- long_passing: nulls=836, int 3..97
  - stats: average=57.0699
- ball_control: nulls=836, int 5..97
  - stats: average=63.3889
- acceleration: nulls=836, int 10..97
  - stats: average=67.6594
- sprint_speed: nulls=836, int 12..97
  - stats: average=68.0512
- agility: nulls=2713, int 11..96
  - stats: average=65.9709
- reactions: nulls=836, int 17..96
  - stats: average=66.1037
- balance: nulls=2713, int 12..96
  - stats: average=65.1895
- shot_power: nulls=836, int 2..97
  - stats: average=61.8084
- jumping: nulls=2713, int 14..96
  - stats: average=66.969
- stamina: nulls=836, int 10..96
  - stats: average=67.0385
- strength: nulls=836, int 10..96
  - stats: average=67.4245
- long_shots: nulls=836, int 1..96
  - stats: average=53.3394
- aggression: nulls=836, int 6..97
  - stats: average=60.948
- interceptions: nulls=836, int 1..96
  - stats: average=52.0093
- positioning: nulls=836, int 2..96
  - stats: average=55.7865
- vision: nulls=2713, int 1..97
  - stats: average=57.8735
- penalties: nulls=836, int 2..96
  - stats: average=55.004
- marking: nulls=836, int 1..96
  - stats: average=46.7722
- standing_tackle: nulls=836, int 1..95
  - stats: average=50.3513
- sliding_tackle: nulls=2713, int 2..95
  - stats: average=48.0015
- gk_diving: nulls=836, int 1..94
  - stats: average=14.7044
- gk_handling: nulls=836, int 1..93
  - stats: average=16.0636
- gk_kicking: nulls=836, int 1..97
  - stats: average=20.9984
- gk_positioning: nulls=836, int 1..96
  - stats: average=16.1322
- gk_reflexes: nulls=836, int 1..96
  - stats: average=16.4414


# Team

```sql
CREATE TABLE "Team" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`team_api_id`	INTEGER UNIQUE,
	`team_fifa_api_id`	INTEGER,
	`team_long_name`	TEXT,
	`team_short_name`	TEXT
);
```

## Rows

- total=299

| column | latest | sample | sample |
|---|---|---|---|
| id | 51606 | 7 | 11074 |
| team_api_id | 7896 | 9991 | 108893 |
| team_fifa_api_id | null | 674 | 111989 |
| team_long_name | Lugano | KAA Gent | AC Arles-Avignon |
| team_short_name | LUG | GEN | ARL |

## Columns

- id: unique identifier, int 1..51606
- team_api_id: unique identifier, int 1601..274581
- team_fifa_api_id: 285 distinct, nulls=11, int 1..112513
- team_long_name: 296 distinct
- team_short_name: 259 distinct


# Team_Attributes

```sql
CREATE TABLE `Team_Attributes` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`team_fifa_api_id`	INTEGER,
	`team_api_id`	INTEGER,
	`date`	TEXT,
	`buildUpPlaySpeed`	INTEGER,
	`buildUpPlaySpeedClass`	TEXT,
	`buildUpPlayDribbling`	INTEGER,
	`buildUpPlayDribblingClass`	TEXT,
	`buildUpPlayPassing`	INTEGER,
	`buildUpPlayPassingClass`	TEXT,
	`buildUpPlayPositioningClass`	TEXT,
	`chanceCreationPassing`	INTEGER,
	`chanceCreationPassingClass`	TEXT,
	`chanceCreationCrossing`	INTEGER,
	`chanceCreationCrossingClass`	TEXT,
	`chanceCreationShooting`	INTEGER,
	`chanceCreationShootingClass`	TEXT,
	`chanceCreationPositioningClass`	TEXT,
	`defencePressure`	INTEGER,
	`defencePressureClass`	TEXT,
	`defenceAggression`	INTEGER,
	`defenceAggressionClass`	TEXT,
	`defenceTeamWidth`	INTEGER,
	`defenceTeamWidthClass`	TEXT,
	`defenceDefenderLineClass`	TEXT,
	FOREIGN KEY(`team_fifa_api_id`) REFERENCES `Team`(`team_fifa_api_id`),
	FOREIGN KEY(`team_api_id`) REFERENCES `Team`(`team_api_id`)
);
```

## Rows

- total=1458

| column | latest | sample | sample |
|---|---|---|---|
| id | 1458 | 463 | 329 |
| team_fifa_api_id | 15005 | 110374 | 1867 |
| team_api_id | 10000 | 8535 | 7869 |
| date | 2015-09-10 00:00:00 | 2015-09-10 00:00:00 | 2014-09-19 00:00:00 |
| buildUpPlaySpeed | 54 | 34 | 40 |
| buildUpPlaySpeedClass | Balanced | Balanced | Balanced |
| buildUpPlayDribbling | 42 | 54 | 53 |
| buildUpPlayDribblingClass | Normal | Normal | Normal |
| buildUpPlayPassing | 51 | 33 | 53 |
| buildUpPlayPassingClass | Mixed | Short | Mixed |
| buildUpPlayPositioningClass | Organised | Organised | Organised |
| chanceCreationPassing | 47 | 68 | 40 |
| chanceCreationPassingClass | Normal | Risky | Normal |
| chanceCreationCrossing | 52 | 51 | 66 |
| chanceCreationCrossingClass | Normal | Normal | Normal |
| chanceCreationShooting | 32 | 53 | 48 |
| chanceCreationShootingClass | Little | Normal | Normal |
| chanceCreationPositioningClass | Organised | Organised | Organised |
| defencePressure | 44 | 58 | 36 |
| defencePressureClass | Medium | Medium | Medium |
| defenceAggression | 58 | 59 | 41 |
| defenceAggressionClass | Press | Press | Press |
| defenceTeamWidth | 37 | 61 | 52 |
| defenceTeamWidthClass | Normal | Normal | Normal |
| defenceDefenderLineClass | Cover | Cover | Cover |

## Columns

- id: unique identifier, int 1..1458
- team_fifa_api_id: 285 distinct, int 1..112513
- team_api_id: 288 distinct, int 1601..274581
- date: "2015-09-10 00:00:00"=245, "2011-02-22 00:00:00"=244, "2014-09-19 00:00:00"=244, "2012-02-22 00:00:00"=242, "2013-09-20 00:00:00"=242, "2010-02-22 00:00:00"=241
- buildUpPlaySpeed: 57 distinct, int 20..80
  - stats: average=52.4623, median=52
- buildUpPlaySpeedClass: "Balanced"=1184, "Fast"=172, "Slow"=102
- buildUpPlayDribbling: 49 distinct, nulls=969, int 24..77
  - stats: average=48.6074, median=49
- buildUpPlayDribblingClass: "Little"=1004, "Normal"=433, "Lots"=21
- buildUpPlayPassing: 58 distinct, int 20..80
  - stats: average=48.4904, median=50
- buildUpPlayPassingClass: "Mixed"=1236, "Short"=128, "Long"=94
- buildUpPlayPositioningClass: "Organised"=1386, "Free Form"=72
- chanceCreationPassing: 50 distinct, int 21..80
  - stats: average=52.1653, median=52
- chanceCreationPassingClass: "Normal"=1231, "Risky"=171, "Safe"=56
- chanceCreationCrossing: 56 distinct, int 20..80
  - stats: average=53.7318, median=53
- chanceCreationCrossingClass: "Normal"=1195, "Lots"=211, "Little"=52
- chanceCreationShooting: 57 distinct, int 22..80
  - stats: average=53.9691, median=53
- chanceCreationShootingClass: "Normal"=1224, "Lots"=197, "Little"=37
- chanceCreationPositioningClass: "Organised"=1309, "Free Form"=149
- defencePressure: 48 distinct, int 23..72
  - stats: average=46.0171, median=45
- defencePressureClass: "Medium"=1243, "Deep"=154, "High"=61
- defenceAggression: 47 distinct, int 24..72
  - stats: average=49.251, median=48
- defenceAggressionClass: "Press"=1274, "Double"=99, "Contain"=85
- defenceTeamWidth: 43 distinct, int 29..73
  - stats: average=52.1859, median=52
- defenceTeamWidthClass: "Normal"=1286, "Wide"=111, "Narrow"=61
- defenceDefenderLineClass: "Cover"=1362, "Offside Trap"=96


# match_view

```sql
CREATE VIEW match_view AS SELECT
    M.id,
    L.name AS league,
    M.season,
    M.match_api_id,
    T.team_long_name AS home_team,
    TM.team_long_name AS away_team,
    M.home_team_goal,
    M.away_team_goal,
    P1.player_name AS home_gk,
    P2.player_name AS home_center_back_1,
    P3.player_name AS home_center_back_2,
    P4.player_name AS home_right_back,
    P5.player_name AS home_left_back,
    P6.player_name AS home_midfield_1,
    P7.player_name AS home_midfield_2,
    P8.player_name AS home_midfield_3,
    P9.player_name AS home_midfield_4,
    P10.player_name AS home_second_forward,
    P11.player_name AS home_center_forward,
    P12.player_name AS away_gk,
    P13.player_name AS away_center_back_1,
    P14.player_name AS away_center_back_2,
    P15.player_name AS away_right_back,
    P16.player_name AS away_left_back,
    P17.player_name AS away_midfield_1,
    P18.player_name AS away_midfield_2,
    P19.player_name AS away_midfield_3,
    P20.player_name AS away_midfield_4,
    P21.player_name AS away_second_forward,
    P22.player_name AS away_center_forward,
    M.goal,
    M.card
FROM
    match M
LEFT JOIN
    league L ON M.league_id = L.id
LEFT JOIN
    team T ON M.home_team_api_id = T.team_api_id
LEFT JOIN
    team TM ON M.away_team_api_id = TM.team_api_id
LEFT JOIN
    player P1 ON M.home_player_1 = P1.player_api_id
LEFT JOIN
    player P2 ON M.home_player_2 = P2.player_api_id
LEFT JOIN
    player P3 ON M.home_player_3 = P3.player_api_id
LEFT JOIN
    player P4 ON M.home_player_4 = P4.player_api_id
LEFT JOIN
    player P5 ON M.home_player_5 = P5.player_api_id
LEFT JOIN
    player P6 ON M.home_player_6 = P6.player_api_id
LEFT JOIN
    player P7 ON M.home_player_7 = P7.player_api_id
LEFT JOIN
    player P8 ON M.home_player_8 = P8.player_api_id
LEFT JOIN
    player P9 ON M.home_player_9 = P9.player_api_id
LEFT JOIN
    player P10 ON M.home_player_10 = P10.player_api_id
LEFT JOIN
    player P11 ON M.home_player_11 = P11.player_api_id
LEFT JOIN
    player P12 ON M.away_player_1 = P12.player_api_id
LEFT JOIN
    player P13 ON M.away_player_2 = P13.player_api_id
LEFT JOIN
    player P14 ON M.away_player_3 = P14.player_api_id
LEFT JOIN
    player P15 ON M.away_player_4 = P15.player_api_id
LEFT JOIN
    player P16 ON M.away_player_5 = P16.player_api_id
LEFT JOIN
    player P17 ON M.away_player_6 = P17.player_api_id
LEFT JOIN
    player P18 ON M.away_player_7 = P18.player_api_id
LEFT JOIN
    player P19 ON M.away_player_8 = P19.player_api_id
LEFT JOIN
    player P20 ON M.away_player_9 = P20.player_api_id
LEFT JOIN
    player P21 ON M.away_player_10 = P21.player_api_id
LEFT JOIN
    player P22 ON M.away_player_11 = P22.player_api_id;
```

## Rows

- total=25979

| column | latest | sample | sample |
|---|---|---|---|
| id | 25979 | 6288 | 20084 |
| league | Switzerland Super League | France Ligue 1 | Scotland Premier League |
| season | 2015/2016 | 2011/2012 | 2009/2010 |
| match_api_id | 1992095 | 1019497 | 820477 |
| home_team | BSC Young Boys | FC Sochaux-Montbéliard | Celtic |
| away_team | FC Basel | Toulouse FC | Hibernian |
| home_team_goal | 4 | 3 | 3 |
| away_team_goal | 3 | 0 | 2 |
| home_gk | Yvon Mvogo | Teddy Richert | Artur Boruc |
| home_center_back_1 | Florent Hadergjonaj | Sebastien Corchia | Mark Wilson |
| home_center_back_2 | Milan Vilotic | Mathieu Philippe Peybernes | Josh Thompson |
| home_right_back | Steve von Bergen | Carlao | Darren O'Dea |
| home_left_back | Jan Lecjaks | David Sauget | Lee Naylor |
| home_midfield_1 | Renato Steffen | Kevin Anin | Niall McGinn |
| home_midfield_2 | Denis Zakaria | Loic Poujol | Scott Brown |
| home_midfield_3 | Alain Rochat | Edouard Butin | Landry N'Guemo |
| home_midfield_4 | Miralem Sulejmani | Marvin Martin | Aiden McGeady |
| home_second_forward | Yuya Kubo | Yassin Mikari | Marc-Antoine Fortune |
| home_center_forward | Alexander Gerndt | Modibo Maiga | Robbie Keane |
| away_gk | Tomas Vaclik | Ali Ahamada | Graham Stack |
| away_center_back_1 | Michael Lang | Pavle Ninkov | null |
| away_center_back_2 | Daniel Hoeegh | Daniel Congre | Paul Hanlon |
| away_right_back | Marek Suchy | Aymen Abdennour | Souleymane Bamba |
| away_left_back | Naser Aliji | Cheikh Mbengue | Ian Murray |
| away_midfield_1 | Taulant Xhaka | Etienne Capoue | David Wotherspoon |
| away_midfield_2 | Zdravko Kuzmanovic | Moussa Sissoko | John Rankin |
| away_midfield_3 | Birkir Bjarnason | Antoine Devaux | Kevin McBride |
| away_midfield_4 | Matias Emilio Delgado | Daniel Omoya Braaten | Derek Riordan |
| away_second_forward | Shkelzen Gashi | Franck Tabanou | Colin Nish |
| away_center_forward | Breel Embolo | Emmanuel Riviere | Anthony Stokes |
| goal | null | null | null |
| card | null | null | null |

## Columns

- id: unique identifier, int 1..25979
- league: "England Premier League"=3040, "France Ligue 1"=3040, "Spain LIGA BBVA"=3040, "Italy Serie A"=3017, "Germany 1. Bundesliga"=2448, "Netherlands Eredivisie"=2448, "Portugal Liga ZON Sagres"=2052, "Poland Ekstraklasa"=1920, "Scotland Premier League"=1824, "Belgium Jupiler League"=1728, "Switzerland Super League"=1422
- season: "2008/2009"=3326, "2015/2016"=3326, "2014/2015"=3325, "2010/2011"=3260, "2012/2013"=3260, "2009/2010"=3230, "2011/2012"=3220, "2013/2014"=3032
- match_api_id: unique identifier, int 483129..2216672
- home_team: 296 distinct
- away_team: 296 distinct
- home_team_goal: 1=8400, 2=6339, 0=5896, 3=3288, 4=1385, 5=457, 6=161, 7=38, 8=9, 9=4, 10=2, int 0..10
- away_team_goal: 1=8989, 0=8687, 2=5146, 3=2145, 4=718, 5=215, 6=63, 7=10, 8=5, 9=1, int 0..9
- home_gk: 894 distinct, nulls=1224
- home_center_back_1: 2397 distinct, nulls=1315
- home_center_back_2: 2360 distinct, nulls=1281
- home_right_back: 2590 distinct, nulls=1323
- home_left_back: 2754 distinct, nulls=1316
- home_midfield_1: 3770 distinct, nulls=1325
- home_midfield_2: 3403 distinct, nulls=1227
- home_midfield_3: 4049 distinct, nulls=1309
- home_midfield_4: 4087 distinct, nulls=1273
- home_second_forward: 3623 distinct, nulls=1436
- home_center_forward: 2880 distinct, nulls=1555
- away_gk: 913 distinct, nulls=1234
- away_center_back_1: 2487 distinct, nulls=1278
- away_center_back_2: 2453 distinct, nulls=1293
- away_right_back: 2642 distinct, nulls=1321
- away_left_back: 2867 distinct, nulls=1335
- away_midfield_1: 3904 distinct, nulls=1313
- away_midfield_2: 3593 distinct, nulls=1235
- away_midfield_3: 4214 distinct, nulls=1341
- away_midfield_4: 4294 distinct, nulls=1328
- away_second_forward: 3872 distinct, nulls=1441
- away_center_forward: 3027 distinct, nulls=1554
- goal: 13225 distinct, nulls=11762
- card: 13777 distinct, nulls=11762
