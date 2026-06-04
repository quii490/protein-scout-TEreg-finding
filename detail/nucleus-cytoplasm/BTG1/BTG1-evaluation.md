---
type: protein-evaluation
gene: "BTG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BTG1 — REJECTED (研究热度过高 (PubMed strict=254，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTG1 |
| 蛋白名称 | Protein BTG1 |
| 蛋白大小 | 171 aa / 19.2 kDa |
| UniProt ID | P62324 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 171 aa / 19.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=254 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002087, IPR033332, IPR036054; Pfam: PF07742 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.0/180** | |
| **归一化总分** | | | **46.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 254 |
| PubMed broad count | 333 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Simplified algorithm for genetic subtyping in diffuse large B-cell lymphoma.. *Signal transduction and targeted therapy*. PMID: 37032379
2. IKZF1(plus) Defines a New Minimal Residual Disease-Dependent Very-Poor Prognostic Profile in Pediatric B-Cell Precursor Acute Lymphoblastic Leukemia.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 29498923
3. BTG1 mutation yields supercompetitive B cells primed for malignant transformation.. *Science (New York, N.Y.)*. PMID: 36656933
4. Emerging role of anti-proliferative protein BTG1 and BTG2.. *BMB reports*. PMID: 35880434
5. Tumor suppressors BTG1 and BTG2: Beyond growth control.. *Journal of cellular physiology*. PMID: 30350856

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.4 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 19.3% |
| 有序区域 (pLDDT>70) 占比 | 70.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.4，有序区 70.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002087, IPR033332, IPR036054; Pfam: PF07742 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT7 | 0.937 | 0.848 | — |
| CNOT8 | 0.857 | 0.847 | — |
| FOXO3 | 0.770 | 0.000 | — |
| PRMT1 | 0.712 | 0.482 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 4，IntAct interactions: 0
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.4 + PDB: 无 | pLDDT=81.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 4 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BTG1 — Protein BTG1，研究基础较多，新颖性有限。
2. 蛋白大小171 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 254 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 254 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62324
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133639-BTG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62324
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
