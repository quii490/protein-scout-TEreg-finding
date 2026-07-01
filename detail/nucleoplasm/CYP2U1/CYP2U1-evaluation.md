---
type: protein-evaluation
gene: "CYP2U1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CYP2U1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CYP2U1 |
| 蛋白名称 | Cytochrome P450 2U1 |
| 蛋白大小 | 544 aa / 62.0 kDa |
| UniProt ID | Q7Z449 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 544 aa |
| 研究新颖性 | 7/10 | x5 | 35.0 | PubMed=69 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cyt_P450; Cyt_P450_CS; Cyt_P450_E_grp-I |
| PPI | 5/10 | x3 | 15.0 | PPI degree=26 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- HPA: Golgi apparatus; Nucleoplasm; Vesicles (Approved)
- PubMed: strict=69, broad=104
- AF pLDDT: 88.1 / PDB: 0
- InterPro: Cyt_P450; Cyt_P450_CS; Cyt_P450_E_grp-I
- Pfam: p450
- PPI degree=26 / ChIP: None
23897027: Hereditary spastic paraplegia: clinico-pathologic features and emerging molecula | 34546337: Implication of folate deficiency in CYP2U1 loss of function. | 33107650: Pseudoxanthoma elasticum overlaps hereditary spastic paraplegia type 56.

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**细胞色素P450单加氧酶的核质定位与非经典功能**：CYP2U1（Cytochrome P450 2U1, 544 aa, UniProt Q7Z449）是CYP2家族成员，催化花生四烯酸（arachidonic acid, AA）及其结合物的ω和ω-1羟基化（PMIDs:14660610, 24563460）。其催化机制依赖血红素铁中心（Cyt_P450 IPR001128, Pfam p450）的经典P450催化循环：底物结合→Fe3+→Fe2+还原→O2结合→第二次电子转移→O-O键断裂→底物羟基化+水生成。HPA数据显示Nucleoplasm Approved级别的核定位（9/10），暗示P450的膜外功能——典型P450酶定位于内质网膜胞质面，通过N端跨膜锚定序列（TM-helix）锚定膜上。核质定位可能反映了蛋白酶解释放的可溶性催化域的再分布。

**花生四烯酸代谢物与核内信号传导**：CYP2U1的ω-羟基化产物为20-羟基花生四烯酸（20-HETE），后者是核内PPARα和PPARγ核受体的配体。PPARγ被20-HETE激活后调控脂代谢基因表达，而PPARγ在ERV和LINE-1启动子区域存在广泛结合——PPARγ-RXR异二聚体识别DR-1型（直接重复）基序（AGGTCA-N-AGGTCA），该基序在过去数百万年中被多种TE捕获和传播。因此CYP2U1可通过其产物20-HETE间接调控PPAR-TE轴。另外，花生四烯酸衍生的环氧二十烷三烯酸（EETs）调控NF-κB活性，而NF-κB是许多TE（如HERV-K和HERV-W LTR）启动子的已知转录激活因子。

**遗传性痉挛性截瘫（SPG56）的核内机制视角**：CYP2U1功能缺失突变导致SPG56型遗传性痉挛性截瘫，这是一种上下运动神经元退行性疾病（PMIDs:23897027, 34546337, 42204580）。SPG56的病理特征为轴突变性和髓鞘异常——若CYP2U1在核内执行AA代谢功能，其丧失可能导致神经细胞核内PPAR信号紊乱，进而影响TE衍生调控元件对神经元基因的表达调控。PMIDs:42046106发现CYP2U1突变者出现以肌张力障碍为首发症状的表型扩展，提示功能缺失的广泛下游影响。

**TE调控的间接药理学可行性**：与小分子抑制剂/激活剂兼容是CYP酶的优势。若核内CYP2U1的AA代谢活性被证实影响TE表达，可通过P450抑制剂（如1-氨基苯并三唑）或20-HETE合成抑制剂进行药理学干预——这在其他TE调控候选（如锌指蛋白或分子伴侣）中通常不可行。归一化得分68.3/100中核定位特异性36/40是主要驱动力。


### 补充分析 (UniProt API)

**蛋白全称**: Cytochrome P450 2U1

**功能**: A cytochrome P450 monooxygenase involved in the metabolism of arachidonic acid and its conjugates (PubMed:14660610, PubMed:24563460). Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (CPR; NADPH-ferrihemoprotein reductase) (PubMed:14660610, PubMed:24563460). Acts as an omega and omega-1 hydroxylase for arachidonic acid and possibly for other long cha

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001128 |
| InterPro | IPR017972 |
| InterPro | IPR002401 |
| InterPro | IPR008069 |
| InterPro | IPR036396 |
| InterPro | IPR050182 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| INS | BioGRID | 0 |
| LGR4 | BioGRID | 0 |
| UBE2H | BioGRID | 0 |