---
type: protein-evaluation
gene: "C6orf223"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C6orf223 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C6orf223 / C6orf223 |
| 蛋白名称 | Uncharacterized protein LINC03040 |
| 蛋白大小 | 242 aa / 26.1 kDa |
| UniProt ID | Q8N319 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 26.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041009; Pfam: PF17704 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf223 |

**关键文献**:
1. C6orf223 promotes colorectal cancer growth and metastasis by facilitating PRMT5-MEP50 multiprotein complex assembling.. *The Journal of clinical investigation*. PMID: 41090362
2. Potential biomarkers: The hypomethylation of cg18949415 and cg22193385 sites in colon adenocarcinoma.. *Computers in biology and medicine*. PMID: 38154158
3. Seven bacterial response-related genes are biomarkers for colon cancer.. *BMC bioinformatics*. PMID: 36941538
4. System analysis of VEGFA in renal cell carcinoma: The expression, prognosis, gene regulation network and regulation targets.. *The International journal of biological markers*. PMID: 34870494
5. AC099850.3 promotes HBV-HCC cell proliferation and invasion through regulating CD276: a novel strategy for sorafenib and immune checkpoint combination therapy.. *Journal of translational medicine*. PMID: 39217342

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.0% |
| 中等置信 (pLDDT 50-70) 占比 | 52.1% |
| 低置信 (pLDDT<50) 占比 | 47.9% |
| 有序区域 (pLDDT>70) 占比 | 0.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.7），有序残基占 0.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041009; Pfam: PF17704 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KCNV2 | 0.575 | 0.000 | — |
| ZADH2 | 0.543 | 0.000 | — |
| TDRP | 0.434 | 0.000 | — |
| ZNF700 | 0.410 | 0.000 | — |
| KRTAP5-7 | 0.407 | 0.000 | — |
| ZFPM2 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 6，IntAct interactions: 0
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.7 + PDB: 无 | pLDDT=49.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 6 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. C6orf223 — Uncharacterized protein LINC03040，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N319
- Protein Atlas: https://www.proteinatlas.org/search/C6orf223
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C6orf223
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N319
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
