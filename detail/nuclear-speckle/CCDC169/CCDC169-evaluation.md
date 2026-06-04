---
type: protein-evaluation
gene: "CCDC169"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC169 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC169 / C13orf38 |
| 蛋白全名 | Coiled-coil domain-containing protein 169 |
| 蛋白大小 | 214 aa / 25.3 kDa |
| UniProt ID | A6NNP5 |
| 子定位分类 | nuclear-speckle |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Nuclear speckles, Vesicles |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 214 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=3 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=80.0, >70%=65.0%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 3/10 | x3 | 9 | 仅有低置信度STRING关联 (15条) |
| 互证加分 | — | max+3 | 0 | 无额外互证加分 |
| **加权总分** | | | **132.0/180** | |
| **归一化总分 (÷1.83)** | | | **72.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Nuclear speckles, Vesicles | Approved |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | 无 | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

214 aa (200-800 aa ideal range)

**评价**: 214 aa / 25.3 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 3 |
| PubMed symbol_only | 4 |
| PubMed broad | 4 |
| 别名 | C13orf38 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 3 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Identification of a Five-Gene Panel to Assess Prognosis for Gastric Cancer.** *BioMed research international* (2022) PMID:35187167 -- Li S et al.
2. **Identification of Thrombosis-Related Genes in Patients with Advanced Gastric Cancer: Data from AGAMENON-SEOM Registry.** *Biomedicines* (2022 Jan 11) PMID:35052827 -- Zaragoza-Huesca D et al.
3. **Induced Chromosomal Aneuploidy Results in Global and Consistent Deregulation of the Transcriptome of Cancer Cells.** *Neoplasia (New York, N.Y.)* (2019 Jul) PMID:31174021 -- Wangsa D et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 80.0 |
| pLDDT > 90 (Very High) | 50.0% |
| pLDDT 70-90 (High) | 15.0% |
| pLDDT 50-70 (Medium) | 28.0% |
| pLDDT < 50 (Low) | 7.0% |
| 有序区域 (pLDDT>70) 占比 | 65.0% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=80.0，有序区域 65%）。作为新颖蛋白，此水平可接受。

**评分: 7/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| SOHLH2 | 0.522 | 0.000 | — |
| TMEM161B | 0.509 | 0.000 | — |
| CCDC190 | 0.478 | 0.000 | — |
| CCDC74B | 0.476 | 0.000 | — |
| PROSER1 | 0.475 | 0.000 | — |
| MAB21L1 | 0.471 | 0.000 | — |
| CCDC125 | 0.453 | 0.000 | — |
| STPG2 | 0.448 | 0.000 | — |
| ZNF287 | 0.430 | 0.000 | — |
| ZNF641 | 0.428 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| — | — | — | — |


**已知复合体成员** (GO Cellular Component):
- 无GO-CC注释

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 0
- 调控相关比例: 0/15 (0%)

**评价**: 仅有低置信度STRING关联 (15条)

**评分: 3/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 0 | 数据有限 |

**互证加分明细**:
- 无额外互证加分
**总分**: 0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (72.1/100)

**核心优势**:
1. Extremely novel -- PubMed=3篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NNP5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC169
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NNP5
- STRING: https://string-db.org/cgi/network?identifiers=CCDC169&species=9606
