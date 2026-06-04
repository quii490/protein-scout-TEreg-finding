---
type: protein-evaluation
gene: "MSC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MSC — REJECTED (研究热度过高 (PubMed strict=9376，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSC / ABF1, BHLHA22 |
| 蛋白名称 | Musculin |
| 蛋白大小 | 206 aa / 22.1 kDa |
| UniProt ID | O60682 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 206 aa / 22.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=9376 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9376 |
| PubMed broad count | 50962 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ABF1, BHLHA22 |

**关键文献**:
1. MSC exosome works through a protein-based mechanism of action.. *Biochemical Society transactions*. PMID: 29986939
2. Single-cell transcriptome atlas of human mesenchymal stem cells exploring cellular heterogeneity.. *Clinical and translational medicine*. PMID: 34965030
3. Human umbilical cord mesenchymal stem cell-derived exosomes ameliorate liver steatosis by promoting fatty acid oxidation and reducing fatty acid synthesis.. *JHEP reports : innovation in hepatology*. PMID: 37274776
4. Mesenchymal stem versus stromal cells: International Society for Cell & Gene Therapy (ISCT®) Mesenchymal Stromal Cell committee position statement on nomenclature.. *Cytotherapy*. PMID: 31526643
5. Mesenchymal Stem Cell Engineering.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 38270877

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.4 |
| 高置信度残基 (pLDDT>90) 占比 | 21.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.7% |
| 中等置信 (pLDDT 50-70) 占比 | 39.3% |
| 低置信 (pLDDT<50) 占比 | 29.1% |
| 有序区域 (pLDDT>70) 占比 | 31.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.4），有序残基占 31.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HES6 | 0.817 | 0.094 | — |
| AKR7A3 | 0.745 | 0.000 | — |
| MYF5 | 0.720 | 0.067 | — |
| TCF3 | 0.714 | 0.291 | — |
| MYOD1 | 0.711 | 0.067 | — |
| TCF4 | 0.695 | 0.400 | — |
| NKX3-2 | 0.689 | 0.071 | — |
| ID2 | 0.640 | 0.297 | — |
| SIRT2 | 0.635 | 0.000 | — |
| TLX1 | 0.634 | 0.046 | — |

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
| 三维结构 | AlphaFold pLDDT=64.4 + PDB: 无 | pLDDT=64.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MSC — Musculin，研究基础较多，新颖性有限。
2. 蛋白大小206 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9376 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 9376 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60682
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178860-MSC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60682
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
