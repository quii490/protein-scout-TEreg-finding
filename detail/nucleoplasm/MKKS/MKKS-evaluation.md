---
type: protein-evaluation
gene: "MKKS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
rejection_reason: "PubMed strict count 196 > 100 — research novelty threshold exceeded"
---

## MKKS 核蛋白评估（淘汰）

### 基本信息

| 属性 | 值 |
|------|-----|
| 基因名 | MKKS (BBS6) |
| UniProt Accession | Q9NPJ1 |
| 蛋白全称 | Molecular chaperone MKKS (McKusick-Kaufman syndrome protein) |
| 氨基酸长度 | 570 aa |
| 分子量 | 62.3 kDa |
| 功能摘要 | Probable molecular chaperone assisting protein folding upon ATP hydrolysis. Plays a role in BBSome assembly, a complex involved in ciliogenesis regulating vesicle transport to cilia. May play a role in protein processing in limb, cardiac, and reproductive system development. Associated with McKusick-Kaufman syndrome and Bardet-Biedl syndrome (as BBS6). |

### 淘汰判定

| 淘汰规则 | 阈值 | 实际值 | 触发 |
|----------|------|--------|------|
| PubMed strict count > 100 | ≤100 | 196 | **是** |
| 核定位特异性 ≤ 3 | ≥4 | 4 | 否 |

**结论**: PubMed strict count = 196，远超100篇门槛。MKKS/BBS6作为Bardet-Biedl综合征的关键基因，已被广泛研究，涉及纤毛发生、BBSome组装、分子伴侣功能等经典领域。研究新颖性不足，不适宜作为TE调控新靶点。

---

### 多维度评分

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 4/10 | ×4 | 16 | UniProt Nucleus (ECO:0000269) + centrosome/cytosol。GO-CC nucleus IDA:UniProtKB。但HPA IF显示主定位为Centrosome+Basal body，不包含核信号。UniProt与HPA定位冲突。 |
| 蛋白大小 | 5/10 | ×1 | 5 | 570 aa, 62.3 kDa。中等大小，属于type II chaperonin家族。 |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=196 (query: "MKKS"[Title/Abstract] AND gene/protein/hydrolase)，broad=255，symbol_only=229。远超100篇淘汰线。 |
| 三维结构 | 5/10 | ×3 | 15 | 无实验PDB结构。AlphaFold mean pLDDT=89.0，pct_gt_90=64.6%，pct_lt_50仅0.7%，预测结构置信度极高。属chaperonin折叠，可能以寡聚体形式发挥功能。 |
| 调控结构域 | 6/10 | ×2 | 12 | Type II chaperonin (TCP-1/CCT家族): IPR002423 (Cpn60/TCP-1), IPR027409 (GroEL-like apical domain), IPR027413 (GroEL-like equatorial domain), IPR027410 (TCP-1-like intermediate domain)。Pfam PF00118。结构域注释丰富且功能明确。 |
| PPI网络 | 6/10 | ×3 | 18 | STRING: CCT复合物全亚基(CCT2-8, TCP1) + BBSome组分(BBS2, BBS7, BBS10, BBS12)。IntAct实验验证：BBS7, TCP1, CCT2, BBS10, BBS2, BBS12(均CoIP, PMID:22500027)。功能网络清晰完整。 |
| **加权总分** | | | **66/180** | |
| **归一化总分 (÷1.8)** | | | **36.7/100** | |

---

### 核定位详细分析

**UniProt 亚细胞定位**:
- Cytoplasm, cytoskeleton, microtubule organizing center, centrosome
- Cytoplasm, cytosol (ECO:0000269 — experimental evidence from PubMed)
- Nucleus (ECO:0000269 — experimental evidence from PubMed)

**GO-CC 细胞组分**:
- GO:0005813 centrosome (IDA:HPA)
- GO:0036064 ciliary basal body (IDA:HPA)
- GO:0005737 cytoplasm (IDA:UniProtKB)
- GO:0005829 cytosol (IEA:UniProtKB-SubCell)
- GO:1902636 kinociliary basal body (IBA:GO_Central)
- GO:0031514 motile cilium (ISS:BHF-UCL)
- GO:0005634 nucleus (IDA:UniProtKB)

**HPA 免疫荧光**:
- 可靠性: Supported
- 主定位: Centrosome, Basal body
- 附加定位: (无)
- IF图像: 可用（12张blue_red_green IF原图）

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

关键矛盾：UniProt列出的nucleus定位有实验证据(ECO:0000269)支持，GO-CC中nucleus的注释来源为IDA:UniProtKB。然而，HPA免疫荧光的主要信号位于centrosome和basal body（纤毛基体），并未报告核定位信号。这种不一致可能反映出：(1) MKKS在特定条件下才进入核内（如细胞周期特定时相或应激条件）；(2) HPA的抗体可能因为表位遮蔽而未能检测到核内MKKS。HPA的"Supported"可靠性等级低于"Enhanced"和"Approved"，提示数据一致性可能存在问题。

由于HPA未能验证核定位，且已知功能集中在centrosome和cilia相关过程，核定位特异性仅得4分。

---

### 三维结构分析

**AlphaFold 预测**:
- Entry: AF-Q9NPJ1-F1 (version 6)
- Mean pLDDT: 89.0
- pLDDT >90: 64.6%
- pLDDT 70-90: 26.5%
- pLDDT 50-70: 8.2%
- pLDDT <50: 0.7%

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。pLDDT统计显示该蛋白具有极高的结构置信度：64.6%残基pLDDT>90，仅0.7%残基pLDDT<50。这与其作为chaperonin家族成员的折叠特性一致——分子伴侣通常具有高度有序的三维结构。

**实验结构**: 无PDB条目。MKKS尚未有实验解析的三维结构。作为type II chaperonin (CCT/TRiC复合物相关)，MKKS的功能形式可能为寡聚体，单体实验结构解析的缺失可能与此有关。AlphaFold预测仅涵盖单体构象。

---

### 调控结构域分析

| 数据库 | 条目 | 名称 |
|--------|------|------|
| InterPro | IPR002423 | Chaperonin Cpn60/GroEL/TCP-1 family |
| InterPro | IPR027409 | GroEL-like apical domain superfamily |
| InterPro | IPR027413 | GroEL-like equatorial domain superfamily |
| InterPro | IPR028790 | MKKS/BBS6 |
| InterPro | IPR027410 | TCP-1-like chaperonin intermediate domain superfamily |
| Pfam | PF00118 | TCP-1/cpn60 chaperonin family |

MKKS属于type II chaperonin家族，与CCT/TRiC复合物各亚基(CCT1-8)共享折叠模式。经典chaperonin含三个结构域：
- **Apical domain**: 负责底物识别和结合
- **Intermediate domain**: 连接apical和equatorial，传递ATP水解的构象变化
- **Equatorial domain**: 含ATP结合和水解位点，介导寡聚化

MKKS作为BBSome组装过程中的分子伴侣，协助BBS蛋白的正确折叠和复合物组装。MKKS突变导致蛋白质错误折叠并经由CHIP介导的泛素化途径降解(PMID:18094050)，证实了其分子伴侣功能的结构基础。

---

### PPI 网络分析

**STRING 数据库 Top 15 互作伴侣**:

| 伴侣基因 | 综合得分 | 实验得分 | 数据库得分 | 文本挖掘 |
|----------|----------|----------|------------|----------|
| CCT2 | 0.994 | 0.787 | 0.876 | 0.331 |
| CCT5 | 0.990 | 0.693 | 0.876 | 0.298 |
| CCT8 | 0.966 | 0.615 | 0.851 | 0.138 |
| BBS12 | 0.966 | 0.780 | 0.800 | 0.303 |
| CCT3 | 0.956 | 0.616 | 0.851 | 0.141 |
| CCT4 | 0.950 | 0.625 | 0.851 | 0.152 |
| BBS10 | 0.929 | 0.516 | 0.800 | 0.314 |
| TCP1 | 0.924 | 0.516 | 0.800 | 0.257 |
| CCT7 | 0.922 | 0.585 | 0.408 | 0.116 |
| HSPE1 | 0.798 | 0.470 | 0 | 0.172 |
| CCT6A | 0.788 | 0.497 | 0 | 0.104 |
| CCT8L2 | 0.780 | 0.479 | 0.290 | 0.138 |
| CCT6B | 0.778 | 0.497 | 0 | 0.104 |
| BBS2 | 0.775 | 0.510 | 0.400 | 0.293 |
| BBS7 | 0.750 | 0.510 | 0.400 | 0.204 |

**IntAct 实验互作（已验证）**:

| 互作伴侣 | 方法 | PMID |
|----------|------|------|
| BBS7 | anti-tag coimmunoprecipitation | 22500027 |
| TCP1 | anti-tag coimmunoprecipitation | 22500027 |
| CCT2 | anti-tag coimmunoprecipitation | 22500027 |
| BBS10 | anti-tag coimmunoprecipitation | 22500027 |
| BBS2 | anti-tag coimmunoprecipitation | 22500027 |
| BBS12 | anti-tag coimmunoprecipitation | 22500027 |
| ZBED1 | two hybrid array | 32296183 |
| CDR2 | two hybrid array | 32296183 |
| HSCB | anti-bait coimmunoprecipitation | 28380382 |
| EEF1G | anti-tag coimmunoprecipitation | 28514442 |
| STK16 | anti-bait coimmunoprecipitation | 17353931 |
| TGIF1 | anti-bait coimmunoprecipitation | 17353931 |
| ICA1 | anti-bait coimmunoprecipitation | 17353931 |

PPI网络呈现清晰的二分结构：(1) CCT/TRiC伴侣蛋白复合物各亚基——反映了MKKS作为type II chaperonin与标准伴侣蛋白机器的物理关联；(2) BBSome组分(BBS2, BBS7, BBS10, BBS12)——反映其在纤毛发生过程中的BBS伴侣功能。Seo et al. (2010, PMID:20080638)系统的CoIP实验证实了MKKS与BBS10/BBS12的BBS-chaperonin复合物形成。

---

### 关键文献

1. **PMID: 20080638** — Seo S et al. (2010) "BBS6, BBS10, and BBS12 form a complex with CCT/TRiC family chaperonins and mediate BBSome assembly." *PNAS*. 核心文献：证实MKKS与BBS10、BBS12及CCT/TRiC伴侣蛋白形成复合物，介导BBSome组装。

2. **PMID: 18094050** — Hirayama S et al. (2008) "MKKS is a centrosome-shuttling protein degraded by disease-causing mutations via CHIP-mediated ubiquitination." *Molecular Biology of the Cell*. 阐明MKKS的中心体穿梭机制和致病突变的降解途径。

3. **PMID: 22446187** — Rachel RA et al. (2012) "Combining Cep290 and Mkks ciliopathy alleles in mice rescues sensory defects and restores ciliogenesis." *Journal of Clinical Investigation*. 小鼠模型中的遗传互作研究。

4. **PMID: 18813213** — Rouskas K et al. (2008) "Association between BBS6/MKKS gene polymorphisms, obesity and metabolic syndrome in the Greek population." *International Journal of Obesity*. MKKS多态性与代谢综合征的人群遗传学关联。

5. **PMID: 28753627** — May-Simera HL et al. (2017) "MKKS/BBS6 in cytokinesis." 证实MKKS在胞质分裂中的功能。

---

### HPA IF 图像

HPA IF 原图已从HPA网站获取（12张IF原图），但未下载到本地。HPA主定位：Centrosome, Basal body。无核定位信号。可靠性：Supported。

---

### 最终决定

**REJECTED** — PubMed strict count = 196，远超100篇上限。MKKS/BBS6是Bardet-Biedl综合征和McKusick-Kaufman综合征的经典致病基因，在最临床遗传学、纤毛生物学、分子伴侣领域已有数十年研究历史。其功能定位以中心体和纤毛基体为主，核定位证据存在但受HPA IF数据矛盾的影响。作为高度成熟的研究对象，不满足TE调控新靶点的筛选条件。

---

### 人工审核备注

- MKKS定位于染色体20p12.2，编码type II chaperonin
- BBSome组装机制已被多篇Nature/Science/PNAS级论文阐明
- BBS6(BBS10,BBS12)-CCT/TRiC轴是纤毛生物学的经典范式
- 核定位证据存在但与HPA主定位(centrosome/basal body)冲突
- AlphaFold结构置信度极佳(mean pLDDT 89.0)，但无实验结构
- PPI网络以CCT复合物和BBSome为核心，功能明确
- 自上次thin-reject后重新评估：harvest数据完整，因PubMed>100仍被淘汰

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000125863-MKKS/subcellular

![](https://images.proteinatlas.org/44233/2120_B7_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/44233/2120_B7_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/44233/2131_C10_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/44233/2131_C10_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/44233/2168_D9_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/44233/2168_D9_68_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
