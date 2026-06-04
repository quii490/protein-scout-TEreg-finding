---
type: protein-evaluation
gene: "BPGM"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## BPGM 核蛋白评估报告（HPA复核救回）

**IF 图像

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/BPGM/IF_images/A431_2.jpg]]**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/BPGM/IF_images/A431_1.jpg]]

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli rim; Nucleoli; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | BPGM |
| 蛋白名称 | Bisphosphoglycerate mutase |
| 蛋白大小 | 259 aa |
| UniProt ID | [P07738](https://www.uniprot.org/uniprotkb/P07738) |
| HPA 核定位 (IF) | Nucleoli rim; Nucleoli; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 63 |
| AlphaFold pLDDT | 95.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli rim; Nucleoli; Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 259 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 63篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 95.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **106/183** |  |
| **归一化总分** |  |  | **57.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 BPGM 定位：
- **亚细胞定位**: Nucleoli rim; Nucleoli; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ; 

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/BPGM/BPGM-PAE.png]]

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Scicluna BP et al. (2017). "Classification of patients with sepsis according to blood genomic endotype: a prospective cohort study". *Lancet Respir Med*. PMID: 28864056
2. Wang J et al. (2025). "Single-cell metabolomics reveals that bisphosphoglycerate mutase influences oocyte maturation through glucose metabolism". *Mol Hum Reprod*. PMID: 40323314
3. Zhang J et al. (2026). "Hepatocyte BPGM Induces RET Lactylation and Macrophage Reprogramming to Promote Tumorigenesis in Hepatocellular Carcinoma". *Adv Sci (Weinh)*. PMID: 41514495
4. Yu F et al. (2025). "Longevity Humans Have Youthful Erythrocyte Function and Metabolic Signatures". *Aging Cell*. PMID: 39924931
5. Kulow VA et al. (2025). "Beyond hemoglobin: Critical role of 2,3-bisphosphoglycerate mutase in kidney function and injury". *Acta Physiol (Oxf)*. PMID: 39422260

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ATP4B | two hybrid array | 21988832 | — | — |
| CEL | two hybrid array | 21988832 | — | — |
| EGR2 | two hybrid array | 21988832 | — | — |
| EHD2 | two hybrid array | 21988832 | — | — |
| NEK3 | two hybrid array | 21988832 | — | — |
| ATF6 | two hybrid array | 21988832 | — | — |
| GRB2 | two hybrid | 18624398 | — | — |
| AKT1 | two hybrid | 18624398 | — | — |
| PGAM2 | two hybrid prey pooling approach | 32296183 | — | — |
| Zap70 | pull down | 31585087 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 11 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli rim; Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅63篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 95.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/BPGM)
- [UniProt](https://www.uniprot.org/uniprotkb/P07738)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=BPGM%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P07738)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[BPGM-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/BPGM/BPGM-PAE.png]]




