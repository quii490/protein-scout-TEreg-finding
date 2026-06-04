---
type: protein-evaluation
gene: "DGUOK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DGUOK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGUOK / DGK |
| 蛋白名称 | Deoxyguanosine kinase, mitochondrial |
| 蛋白大小 | 277 aa / 32.1 kDa |
| UniProt ID | Q16854 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 277 aa / 32.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.1; PDB: 2OCP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002624, IPR050566, IPR031314, IPR027417; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 147 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DGK |

**关键文献**:
1. Transcriptional Regulation of De Novo Lipogenesis by SIX1 in Liver Cancer Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39258807
2. Deoxyguanosine kinase deficiency: natural history and liver transplant outcome.. *Brain communications*. PMID: 38756539
3. Mitochondrial DNA maintenance defects.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 28215579
4. Lactate-related gene signatures predict prognosis and immune profiles in esophageal squamous cell carcinoma.. *Scientific reports*. PMID: 40617965
5. Severe mtDNA depletion and dependency on catabolic lipid metabolism in DGUOK knockout mice.. *Human molecular genetics*. PMID: 31127938

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.1 |
| 高置信度残基 (pLDDT>90) 占比 | 73.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 13.4% |
| 有序区域 (pLDDT>70) 占比 | 83.7% |
| 可用 PDB 条目 | 2OCP |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.1，有序区 83.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002624, IPR050566, IPR031314, IPR027417; Pfam: PF01712 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

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
| 三维结构 | AlphaFold pLDDT=86.1 + PDB: 2OCP | pLDDT=86.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DGUOK — Deoxyguanosine kinase, mitochondrial，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小277 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16854
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114956-DGUOK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGUOK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16854
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
