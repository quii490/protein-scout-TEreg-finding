---
type: protein-evaluation
gene: "SMYD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMYD2 — REJECTED (研究热度过高 (PubMed strict=167，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMYD2 / KMT3C |
| 蛋白名称 | N-lysine methyltransferase SMYD2 |
| 蛋白大小 | 433 aa / 49.7 kDa |
| UniProt ID | Q9NRG4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Mitochondria; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 433 aa / 49.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=167 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.4; PDB: 3RIB, 3S7B, 3S7D, 3S7F, 3S7J, 3TG4, 3TG5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050869, IPR001214, IPR046341, IPR044419, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Mitochondria | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 167 |
| PubMed broad count | 235 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KMT3C |

**关键文献**:
1. SMYD2-Methylated PPARγ Facilitates Hypoxia-Induced Pulmonary Hypertension by Activating Mitophagy.. *Circulation research*. PMID: 38770649
2. Lysine methyltransferase SMYD2 promotes cyst growth in autosomal dominant polycystic kidney disease.. *The Journal of clinical investigation*. PMID: 28604386
3. Methylation of ESCRT-III components regulates the timing of cytokinetic abscission.. *Nature communications*. PMID: 38740816
4. SMYD2 induced PGC1α methylation promotes stemness maintenance of glioblastoma stem cells.. *Neuro-oncology*. PMID: 38721826
5. Histone methyltransferase SMYD2: ubiquitous regulator of disease.. *Clinical epigenetics*. PMID: 31370883

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.4 |
| 高置信度残基 (pLDDT>90) 占比 | 98.2% |
| 置信残基 (pLDDT 70-90) 占比 | 0.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.2% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 99.1% |
| 可用 PDB 条目 | 3RIB, 3S7B, 3S7D, 3S7F, 3S7J, 3TG4, 3TG5, 4O6F, 4WUY, 4YND |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3RIB, 3S7B, 3S7D, 3S7F, 3S7J, 3TG4, 3TG5, 4O6F, 4WUY, 4YND）+ AlphaFold极高置信度预测（pLDDT=97.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050869, IPR001214, IPR046341, IPR044419, IPR011990; Pfam: PF00856, PF01753 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TP53 | 0.989 | 0.891 | — |
| HSP90AA1 | 0.928 | 0.515 | — |
| SETD7 | 0.860 | 0.000 | — |
| HSP90AB1 | 0.856 | 0.051 | — |
| CAMKMT | 0.826 | 0.000 | — |
| KMT5A | 0.786 | 0.071 | — |
| H3C12 | 0.734 | 0.151 | — |
| H3C13 | 0.734 | 0.151 | — |
| SETD3 | 0.726 | 0.000 | — |
| KDM1A | 0.709 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SF3A1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSK3B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSKIP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000355924.5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ASPM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RADIL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ZNF512B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDC37 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IGF2BP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYH6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.4 + PDB: 3RIB, 3S7B, 3S7D, 3S7F, 3S7J,  | pLDDT=97.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Cytosol; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SMYD2 — N-lysine methyltransferase SMYD2，研究基础较多，新颖性有限。
2. 蛋白大小433 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 167 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 167 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRG4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143499-SMYD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMYD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRG4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03





<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000143499-SMYD2/subcellular

![](https://images.proteinatlas.org/29023/2180_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29023/2180_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/29023/273_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29023/273_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29023/275_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29023/275_B9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRG4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRG4 |
| SMART | SM00317; |
| UniProt Domain [FT] | DOMAIN 7..241; /note="SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00190" |
| InterPro | IPR050869;IPR001214;IPR046341;IPR044419;IPR011990;IPR002893; |
| Pfam | PF00856;PF01753; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143499-SMYD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC37 | Intact, Biogrid | true |
| CILK1 | Intact, Biogrid | true |
| PTGES3 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| BTF3 | Biogrid | false |
| BTF3L4 | Intact | false |
| EPB41L3 | Biogrid | false |
| HSP90AA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
