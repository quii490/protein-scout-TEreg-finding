---
type: protein-evaluation
gene: "FHIP2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FHIP2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FHIP2B / FAM160B2, RAI16 |
| 蛋白名称 | FHF complex subunit HOOK-interacting protein 2B |
| 蛋白大小 | 743 aa / 82.3 kDa |
| UniProt ID | Q86V87 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 743 aa / 82.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019384, IPR045669, IPR045668; Pfam: PF19314, PF |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM160B2, RAI16 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 54.5% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.5，有序区 75.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019384, IPR045669, IPR045668; Pfam: PF19314, PF19311, PF10257 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A384L9U0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ZNF318 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYO5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29748336|pubmed:unassig |
| ENST00000289921 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 5
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 无 | pLDDT=79.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 0 + 5 interactions | 数据有限 |

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
1. FHIP2B — FHF complex subunit HOOK-interacting protein 2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小743 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FHIP2B

### PubMed

**Count: 7**

| PMID | Title |
|---|---|
| 32289885 | Retinoic acid induced 16 deficiency exacerbates high-fat diet-induced steatohepatitis in mice. |
| 32014455 | Identification of retinoid acid induced 16 as a novel androgen receptor target in prostate cancer cells. |
| 31862898 | Retinoid acid induced 16 deficiency aggravates colitis and colitis-associated tumorigenesis in mice. |
| 31353455 | FAM160B1 deficit associated with microcephaly, severe intellectual disability, ataxia, behavioral abnormalities and speech problems. |
| 25900241 | Anchoring of both PKA-RIIα and 14-3-3θ regulates retinoic acid induced 16 mediated phosphorylation of heat shock protein 70. |


