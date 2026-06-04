---
type: protein-evaluation
gene: "IQCK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IQCK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IQCK |
| 蛋白名称 | IQ domain-containing protein K |
| 蛋白大小 | 287 aa / 33.3 kDa |
| UniProt ID | Q8N0W5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 287 aa / 33.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043408 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.5/180** | |
| **归一化总分** | | | **73.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic meta-analysis of diagnosed Alzheimer's disease identifies new risk loci and implicates Aβ, tau, immunity and lipid processing.. *Nature genetics*. PMID: 30820047
2. Diverse human astrocyte and microglial transcriptional responses to Alzheimer's pathology.. *Acta neuropathologica*. PMID: 34767070
3. Robust Increase in IQCK Protein Expression in Mouse Models of Alzheimer's Disease and iPSC-Derived Neurons.. *Journal of cellular and molecular medicine*. PMID: 40604342
4. Structural variants linked to Alzheimer's disease and other common age-related clinical and neuropathologic traits.. *Genome medicine*. PMID: 40038788
5. Core genes and immune dysregulation in primary open-angle glaucoma: A molecular insight.. *Technology and health care : official journal of the European Society for Engineering and Medicine*. PMID: 40077931

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 34.8% |
| 有序区域 (pLDDT>70) 占比 | 55.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.7，有序区 55.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043408 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KNOP1 | 0.752 | 0.000 | — |
| GPRC5B | 0.675 | 0.000 | — |
| EFCAB11 | 0.663 | 0.000 | — |
| MCTP1 | 0.562 | 0.000 | — |
| CCDC150 | 0.513 | 0.000 | — |
| LRRC43 | 0.489 | 0.000 | — |
| ABCA7 | 0.474 | 0.000 | — |
| FAM181A | 0.463 | 0.000 | — |
| DTNA | 0.456 | 0.000 | — |
| MAP4K3 | 0.456 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 无 | pLDDT=70.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. IQCK — IQ domain-containing protein K，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小287 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N0W5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174628-IQCK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IQCK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N0W5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
