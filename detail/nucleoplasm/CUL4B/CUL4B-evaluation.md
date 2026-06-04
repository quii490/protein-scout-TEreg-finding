---
type: protein-evaluation
gene: "CUL4B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CUL4B — REJECTED (研究热度过高 (PubMed strict=201，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CUL4B / KIAA0695 |
| 蛋白名称 | Cullin-4B |
| 蛋白大小 | 913 aa / 104.0 kDa |
| UniProt ID | Q13620 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 913 aa / 104.0 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=201 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=78.5; PDB: 2DO7, 4A0C, 4A0L, 4A64, 8EI1 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR045093, IPR059120, IPR016157, IPR016158, IPR036 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- Cul4A-RING E3 ubiquitin ligase complex (GO:0031464)
- Cul4B-RING E3 ubiquitin ligase complex (GO:0031465)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 201 |
| PubMed broad count | 320 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0695 |

**关键文献**:
1. PHIP-associated Chung-Jansen syndrome: Report of 23 new individuals.. *Frontiers in cell and developmental biology*. PMID: 36726590
2. CUL4B protects kidneys from acute injury by restraining p53/PAI-1 signaling.. *Cell death & disease*. PMID: 39695153
3. Depletion of CUL4B in macrophages ameliorates diabetic kidney disease via miR-194-5p/ITGA9 axis.. *Cell reports*. PMID: 37224018
4. MEN1 Degradation Induced by Neddylation and the CUL4B-DCAF7 Axis Promotes Pancreatic Neuroendocrine Tumor Progression.. *Cancer research*. PMID: 36939378
5. Renal tubular GSDME protects cisplatin nephrotoxicity by impeding OGT-STAT3-S100A7A axis in male mice.. *Nature communications*. PMID: 40707439

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.5 |
| 高置信度残基 (pLDDT>90) 占比 | 58.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 21.2% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 2DO7, 4A0C, 4A0L, 4A64, 8EI1 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=78.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045093, IPR059120, IPR016157, IPR016158, IPR036317; Pfam: PF00888, PF26557, PF10557 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCAF1 | 0.999 | 0.828 | — |
| CUL4A | 0.999 | 0.850 | — |
| DTL | 0.999 | 0.888 | — |
| CRBN | 0.999 | 0.828 | — |
| DDB1 | 0.999 | 0.999 | — |
| RBX1 | 0.999 | 0.993 | — |
| DDB2 | 0.998 | 0.880 | — |
| DET1 | 0.998 | 0.804 | — |
| CAND1 | 0.997 | 0.979 | — |
| DCAF11 | 0.996 | 0.846 | — |

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
| 三维结构 | AlphaFold pLDDT=78.5 + PDB: 2DO7, 4A0C, 4A0L, 4A64, 8EI1 | pLDDT=78.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CUL4B -- Cullin-4B，研究基础较多，新颖性有限。
2. 蛋白大小913 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 201 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 201 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13620
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158290-CUL4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CUL4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13620
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
