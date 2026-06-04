---
type: protein-evaluation
gene: "EFS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EFS — REJECTED (研究热度过高 (PubMed strict=1472，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFS / CASS3 |
| 蛋白名称 | Embryonal Fyn-associated substrate |
| 蛋白大小 | 561 aa / 58.8 kDa |
| UniProt ID | O43281 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 561 aa / 58.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1472 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021901, IPR037362, IPR035747, IPR036028, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **67.5/180** | |
| **归一化总分** | | | **37.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- focal adhesion (GO:0005925)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1472 |
| PubMed broad count | 17622 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CASS3 |

**关键文献**:
1. Association between pathologic response and survival after neoadjuvant therapy in lung cancer.. *Nature medicine*. PMID: 37903504
2. Embryonal Fyn-associated substrate (EFS) and CASS4: The lesser-known CAS protein family members.. *Gene*. PMID: 26119091
3. Functional Classification of TP53 Mutations in Acute Myeloid Leukemia.. *Cancers*. PMID: 32164171
4. Tumor Intrinsic Subtypes and Gene Expression Signatures in Early-Stage ERBB2/HER2-Positive Breast Cancer: A Pooled Analysis of CALGB 40601, NeoALTTO, and NSABP B-41 Trials.. *JAMA oncology*. PMID: 38546612
5. Impact of myelodysplasia-related and additional gene mutations in intensively treated patients with NPM1-mutated AML.. *HemaSphere*. PMID: 39816531

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.5 |
| 高置信度残基 (pLDDT>90) 占比 | 29.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 52.8% |
| 有序区域 (pLDDT>70) 占比 | 34.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.5），有序残基占 34.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021901, IPR037362, IPR035747, IPR036028, IPR001452; Pfam: PF12026, PF14604 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FYN | 0.830 | 0.679 | — |
| CSE1L | 0.773 | 0.060 | — |
| CASP3 | 0.739 | 0.094 | — |
| BCL2 | 0.723 | 0.000 | — |
| CRK | 0.712 | 0.366 | — |
| SH2D3C | 0.664 | 0.626 | — |
| CASZ1 | 0.651 | 0.000 | — |
| BLK | 0.622 | 0.591 | — |
| CASS4 | 0.617 | 0.000 | — |
| ACR | 0.537 | 0.097 | — |

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
| 三维结构 | AlphaFold pLDDT=61.5 + PDB: 无 | pLDDT=61.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EFS — Embryonal Fyn-associated substrate，研究基础较多，新颖性有限。
2. 蛋白大小561 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1472 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1472 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43281
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100842-EFS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43281
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
