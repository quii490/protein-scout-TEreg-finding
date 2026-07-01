---
type: protein-evaluation
gene: "DAGLB"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## DAGLB 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DAGLB |
| 蛋白名称 | Diacylglycerol lipase-beta |
| 蛋白大小 | 672 aa / 73.7 kDa |
| UniProt ID | Q8NCG7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 672 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=23 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=72.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | AB_hydrolase_fold; DAG_Lipase-Related; Fungal_lipase-type |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=63 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=23 broad=50
- AF pLDDT=72.5 PDB=0
- InterPro: AB_hydrolase_fold; DAG_Lipase-Related; Fungal_lipase-type
- Pfam: Lipase_3
- PPI degree=63 ChIP: None
35217685: AP-4-mediated axonal transport controls endocannabinoid production in neurons. | 39697748: Prognostic analysis of SYTL4 in acute myeloid leukemia. | 35709154: An approach to quantitate maternal transcripts localized in sea urchin egg corte

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Diacylglycerol lipase-beta

**功能**: Lipase that catalyzes the hydrolysis of arachidonic acid (AA)-esterified diacylglycerols (DAGs) to produce the principal endocannabinoid, 2-arachidonoylglycerol (2-AG) which can be further cleaved by downstream enzymes to release arachidonic acid (AA) for cyclooxygenase (COX)-mediated eicosanoid production (PubMed:14610053). Preferentially hydrolyzes DAGs at the sn-1 position in a calcium-dependent manner and has negligible activity against other lipids including monoacylglycerols and phospholip

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029058 |
| InterPro | IPR052214 |
| InterPro | IPR002921 |
| Pfam | PF01764 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NAPEPLD | STRING | 890 |
| ABHD6 | STRING | 812 |
| PISD | BioGRID | 1 |
| TSPAN5 | BioGRID | 1 |
| VSIG4 | BioGRID | 1 |
| TPCN2 | BioGRID | 1 |
| TSPAN2 | BioGRID | 1 |
| IPPK | BioGRID | 1 |



### 深度机制分析

**结构域架构**：DAGLB（672 aa, 73.7 kDa）为丝氨酸水解酶家族脂酶。AB_hydrolase_fold（IPR029058）含conserved catalytic triad: Ser-Asp-His (GXSXG lipase motif)——水解DAG的sn-1酯键→2-arachidonoylglycerol（2-AG, 体内最丰富的内源性大麻素）。AlphaFold pLDDT=72.5——catalytic core pLDDT>85，N/C端regulatory regions pLDDT~50-65。PPI（degree=63）以内源性大麻素系统为核心：NAPEPLD（STRING score=890）为anandamide合成酶——DAGLB（2-AG合成）与NAPEPLD（AEA合成）协同调控eCB tone；ABHD6（STRING score=812）为2-AG水解酶——DAGLB-ABHD6构成"on-off"开关。2-AG作为retrograde neurotransmitter激活CB1 receptor（Gi/o-coupled GPCR）→cAMP↓→PKA↓→CREB Ser133 phosphorylation↓→抑制CREB-dependent transcription。

**TE调控展望**：TE LTR（HERV-K LTR5_Hs, MMTV LTR）的CRE motif是CREB结合位点——CB1 activation→cAMP↓→CREB-Pi↓→TE LTR transcription下降——DAGLB-generated 2-AG可能抑制CREB-dependent ERV transcription。反之，COX-2将2-AG代谢为PGE2→EP2/EP4 receptor→cAMP↑→PKA→CREB-Pi↑→CREB-dependent TE LTR activation——DAGLB的2-AG产物对TE调控具有双向效应——通过CB1（抑制）或COX-2（促进）途径——取决于炎症微环境和eCB system组成。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NCG7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164535-DAGLB

![](https://images.proteinatlas.org/69377/1314_G12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1314_G12_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1326_G12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1326_G12_5_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164535-DAGLB

![](https://images.proteinatlas.org/69377/1314_G12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1314_G12_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1326_G12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1326_G12_5_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164535-DAGLB

![](https://images.proteinatlas.org/69377/1314_G12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1314_G12_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1326_G12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/69377/1326_G12_5_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 50**

| 42147436 | Long-term consequences of prenatal saccharin exposure: evidence of sex-specific molecular programing in the prefrontal c | Front Behav Neurosci 2026 |
| 41965551 | Distribution and subacute modulation of endocannabinoid metabolizing enzymes in the trigeminal complex and midbrain in a | J Headache Pain 2026 |
| 41788836 | Effects of incubation with endocannabinoids on the expression of endocannabinoid and inflammatory components following a | JDS Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DAGLB

