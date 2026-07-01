---
type: protein-evaluation
gene: "TMEM33"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM33 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM33 |
| 蛋白名称 | Transmembrane protein 33 |
| 蛋白大小 | 247 aa / 28.0 kDa |
| UniProt ID | P57088 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 247 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=26 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=88.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PER33/POM33_regulator; TMEM33/Pom33 |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=155 |
| **加权总分** | | | **122/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +2 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=26, broad=33
- AF pLDDT: 88.4 / PDB: 0
- InterPro: PER33/POM33_regulator; TMEM33/Pom33
- Pfam: TMEM33_Pom33
- PPI degree: 155 / ChIP: None
**Papers**: 31048699: TMEM33 regulates intracellular calcium homeostasis in renal tubular epithelial c | 34487377: PKM2-TMEM33 axis regulates lipid homeostasis in cancer cells by controlling SCAP | 32614325: Interaction mapping of endoplasmic reticulum ubiquitin ligases identifies modula

### 4. 总体评价
★★★★  **67.8/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

**内质网跨膜蛋白的核质溢出与UPR信号转导**：TMEM33（Transmembrane protein 33, 247 aa, UniProt P57088）是定位于管状ER的跨膜蛋白，结构域为PER33/POM33_regulator（IPR051645）和TMEM33/Pom33（IPR005344, Pfam TMEM33_Pom33 PF03661）。其在酵母中的同源物Pom33是核孔复合物跨膜环的关键组分——定位于核孔膜，与Ndc1和Pom152共同构成NPC的膜整合锚定结构。人类TMEM33同样调节管状ER网络，通过刺激PKD2（钙通道）活性和抑制RTN3/4诱导的ER tubule形成来调控ER形态（PMID:25612671）。该蛋白还正向调控PERK和IRE1α介导的未折叠蛋白响应（UPR）信号通路（PMID:26268696），以及VEGF介导的血管新生中ER钙离子释放（PMID:30760708）。

**UPR-ERV调控与TMEM33的潜在连接**：TMEM33的UPR正调控功能直接牵连TE沉默机制——UPR的三条分支（PERK-eIF2α, IRE1α-XBP1s, ATF6）在ERV转录调控中被充分记录：(1) eIF2α磷酸化导致翻译衰减，同时优先翻译ATF4，后者结合LTR中的cAMP应答元件激活HERV转录；(2) XBP1s剪接同工型结合ERV-L和ERV-K LTR中的UPRE基序；(3) ATF6的核质域结合ER应激应答元件（ERSE）——该基序存在于多个HERV LTR中。TMEM33通过增强IRE1α和PERK活性，可能间接上调XBP1s和ATF4/ATF6活性，从而驱动UPR-TE应答轴。另外，TMEM33通过调节ER钙离子稳态和Ca2+释放影响线粒体-ER接触位的代谢通信——钙离子信号已发现调控TE衍生增强子活性（见CALM3）。

**PI3K/AKT/mTOR通路的直接连接**：PMID:42343400（TMEM33 regulates the proliferation and migration of lung adenocarcinoma by promoting the PI3K/AKT/mTOR signaling pathway）直接确证TMEM33与PI3K/AKT/mTOR信号轴的关联。mTORC1通过磷酸化DF-1/ZNFX1调控自噬依赖的TE RNA降解——这是哺乳动物中最古老的TE防御通路之一。PMID:41509280（TMEM33 deletion potentiates anti-tumor CD8+ T cell immunity）进一步暗示TMEM33的缺失促进抗肿瘤CD8+ T细胞免疫——可能与内源性逆转座子（ERV）dsRNA-cGAS-STING通路的去抑制有关。

**ER-phagy的Pom33保守轴**：PMID:40301304（The assembly of RAB22A/TMEM33/RTN4 initiates a secretory ER-phagy pathway）揭示TMEM33与RAB22A和RTN4（Reticulon 4/Nogo）组装起始分泌性ER自噬，将ER组分靶向至自噬融酶体降解。若该ER-phagy通路也降解TE逆转座中间体（在ER膜上发生的cDNA合成和整合），TMEM33可通过"清除-降解"机制限制TE生命周期。PPI degree=155（STRING/BioGRID）反映了其在ER膜蛋白网络中的枢纽地位。归一化得分67.8/100。


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 33

**功能**: Acts as a regulator of the tubular endoplasmic reticulum (ER) network by modulating intracellular calcium homeostasis. Mechanistically, stimulates PKD2 calcium-dependent activity (By similarity). Suppresses the RTN3/4-induced formation of the ER tubules (PubMed:25612671). Positively regulates PERK-mediated and IRE1-mediated unfolded protein response signaling (PubMed:26268696). Plays an essential role in VEGF-mediated release of Ca(2+) from ER stores during angiogenesis (PubMed:30760708). Also p

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR051645 |
| InterPro | IPR005344 |
| Pfam | PF03661 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NDN | BioGRID | 0 |
| PTP4A3 | BioGRID | 0 |
| PPP1CB | BioGRID | 0 |
| BRF2 | BioGRID | 0 |
| USP19 | BioGRID | 0 |
| VCP | BioGRID | 0 |
| MTNR1A | BioGRID | 0 |
| CLN3 | BioGRID | 0 |