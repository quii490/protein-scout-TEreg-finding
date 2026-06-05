---
type: protein-evaluation
gene: "SIK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SIK1 — REJECTED (研究热度过高 (PubMed strict=204，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIK1 / SIK, SNF1LK |
| 蛋白名称 | Serine/threonine-protein kinase SIK1 |
| 蛋白大小 | 783 aa / 84.9 kDa |
| UniProt ID | P57059 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 783 aa / 84.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=204 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 204 |
| PubMed broad count | 310 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SIK, SNF1LK |

**关键文献**:
1. Identification of aging-related biomarkers and immune infiltration characteristics in osteoarthritis based on bioinformatics analysis and machine learning.. *Frontiers in immunology*. PMID: 37503333
2. SIK1 promotes ferroptosis resistance in pancreatic cancer via HDAC5-STAT6-SLC7A11 axis.. *Cancer letters*. PMID: 40250791
3. The AMPK-Related Kinases SIK1 and SIK3 Mediate Key Tumor-Suppressive Effects of LKB1 in NSCLC.. *Cancer discovery*. PMID: 31350328
4. Role of SIK1 in tumors: Emerging players and therapeutic potentials (Review).. *Oncology reports*. PMID: 39422046
5. Integrated Bioinformatics and Experimental Validation Reveal Macrophage Polarization-Related Biomarkers for Osteoarthritis Diagnosis.. *Journal of multidisciplinary healthcare*. PMID: 40765736

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.3 |
| 高置信度残基 (pLDDT>90) 占比 | 32.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 55.8% |
| 有序区域 (pLDDT>70) 占比 | 39.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.3），有序残基占 39.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271, IPR017090; Pfam: PF00069, PF23312 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRTC2 | 0.975 | 0.311 | — |
| SIK1B | 0.901 | 0.000 | — |
| PER1 | 0.838 | 0.000 | — |
| HDAC5 | 0.779 | 0.294 | — |
| CREB1 | 0.725 | 0.066 | — |
| CRTC3 | 0.681 | 0.068 | — |
| SIK2 | 0.670 | 0.444 | — |
| NR4A2 | 0.662 | 0.000 | — |
| NR4A1 | 0.659 | 0.000 | — |
| GINS4 | 0.647 | 0.616 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UTP7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ENP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| KRR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HCA4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UTP10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BMS1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BFR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| PWP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| NOP58 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UTP9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.3 + PDB: 无 | pLDDT=59.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SIK1 — Serine/threonine-protein kinase SIK1，研究基础较多，新颖性有限。
2. 蛋白大小783 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 204 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 204 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57059
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142178-SIK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57059
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/SIK1/IF_images/SIK1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000142178-SIK1/subcellular

![](https://images.proteinatlas.org/78064/1718_A10_13_cr57f3ebf8ac0a0_red_green.jpg)
![](https://images.proteinatlas.org/78064/1718_A10_8_cr57f3ebef59f08_red_green.jpg)
![](https://images.proteinatlas.org/78064/1759_B2_18_cr594b6db621d8c_red_green.jpg)
![](https://images.proteinatlas.org/78064/1759_B2_23_cr594b6dc20872a_red_green.jpg)
![](https://images.proteinatlas.org/78064/1822_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/78064/1822_C12_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P57059-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
