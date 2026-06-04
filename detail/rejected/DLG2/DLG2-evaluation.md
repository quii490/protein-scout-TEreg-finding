---
type: protein-evaluation
gene: "DLG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLG2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLG2 |
| 蛋白名称 | Disks large homolog 2 |
| 蛋白大小 | 870 aa / 97.6 kDa |
| UniProt ID | Q15700 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DLG2/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DLG2/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Vesicles; UniProt: Cell membrane; Postsynaptic density; Synapse; Membrane; Cell |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 870 aa / 97.6 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.9; PDB: 2BYG, 2HE2 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019583, IPR016313, IPR019590, IPR035759, IPR008 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.0/180** | |
| **归一化总分** | | | **58.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Vesicles | Approved |
| UniProt | Cell membrane; Postsynaptic density; Synapse; Membrane; Cell projection, axon; P... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- adherens junction (GO:0005912)
- axon cytoplasm (GO:1904115)
- basolateral plasma membrane (GO:0016323)
- cytosol (GO:0005829)
- juxtaparanode region of axon (GO:0044224)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | N/A |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.9 |
| 高置信度残基 (pLDDT>90) 占比 | 39.1% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 33.2% |
| 有序区域 (pLDDT>70) 占比 | 63.5% |
| 可用 PDB 条目 | 2BYG, 2HE2 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.9），有序残基占 63.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019583, IPR016313, IPR019590, IPR035759, IPR008145; Pfam: PF00625, PF10608, PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.9 + PDB: 2BYG, 2HE2 | pLDDT=69.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Postsynaptic density; Synapse; Memb / Plasma membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DLG2 — Disks large homolog 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小870 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15700
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150672-DLG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15700
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:14:26




