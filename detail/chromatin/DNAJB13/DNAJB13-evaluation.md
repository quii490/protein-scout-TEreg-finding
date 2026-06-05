---
type: protein-evaluation
gene: "DNAJB13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJB13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB13 |
| 蛋白名称 | DnaJ homolog subfamily B member 13 |
| 蛋白大小 | 316 aa / 36.1 kDa |
| UniProt ID | P59910 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Plasma membrane, Mid piece, Principal piece, End piece; 额外: ; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | x1 | 10 | 316 aa / 36.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=36 篇 (<=40->8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=86.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Mid piece, Principal piece, End piece; 额外: Nucleoli, Nucleoli rim, Mitotic chromosome, Vesicles, Primary cilium, Primary cilium tip | Uncertain |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 42 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Small heat shock and J-domain proteins direct defense against areca palm velarivirus 1 by degrading coat protein via autophagy.. *Nat Commun*. PMID: 42049738
2. Normal Fertility of Dnajb13 (exon2 KO)/(exon2 c.106T > C Mut) Compound Heterozygous Mutant Male Mice.. *Reprod Sci*. PMID: 41807802
3. The effects of polysaccharides from Inonotus obliquus, artemisinin, and dihydroartemisinin on the reproductive system of male mice infected with Neospora caninum.. *Front Vet Sci*. PMID: 41800303
4. DNAJB13 polymorphisms and association with idiopathic asthenozoospermia in Sichuan, China.. *Basic Clin Androl*. PMID: 41413469
5. Identifying potential genetic biomarkers for sperm dysfunction through whole-genome sequencing.. *Sci Rep*. PMID: 41115892

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 59.2% |
| 置信残基 (pLDDT 70-90) 占比 | 26.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 5.7% |
| 有序区域 (pLDDT>70) 占比 | 86.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.2，有序区 86.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA6 | 0.000 | 0.000 | — |
| SEPTIN4 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| HSPA4L | 0.000 | 0.000 | — |
| HSPA8 | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 无 | pLDDT=86.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Plasma membrane, Mid piece, Principal piece, End p | 一致 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DNAJB13 -- DnaJ homolog subfamily B member 13，非常新颖，仅有少数基础研究。
2. 蛋白大小316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P59910
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187726-DNAJB13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P59910
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000187726-DNAJB13/subcellular

![](https://images.proteinatlas.org/61330/1694_D9_13_cr580a44762f8ff_blue_red_green.jpg)
![](https://images.proteinatlas.org/61330/1694_D9_18_cr580a445003630_blue_red_green.jpg)
![](https://images.proteinatlas.org/61330/1771_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61330/1771_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61330/1788_G8_10_cr5971fdad05db8_blue_red_green.jpg)
![](https://images.proteinatlas.org/61330/1788_G8_19_cr5971fdad0560c_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P59910-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
