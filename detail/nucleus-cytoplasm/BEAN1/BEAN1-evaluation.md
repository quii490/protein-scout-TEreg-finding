---
type: protein-evaluation
gene: "BEAN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEAN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEAN1 / 无 |
| 蛋白名称 | Protein BEAN1 |
| 蛋白大小 | 259 aa / 28.6 kDa |
| UniProt ID | Q3B7T3 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:33:25 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 259 aa / 28.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (<=20->10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=58.8 |
| 调控结构域 | 3/10 | x2 | 6 | InterPro: 1; Pfam: 0; IPR039352 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **140.5/180** | |
| **归一化总分 (/1.83)** | | | **76.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Centrosome | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 24 |

**关键文献**:
1. Hereditary Ataxia Overview.. **. PMID: 20301317
2. Elevated BEAN1 expression correlates with poor prognosis, immune evasion, and chemotherapy resistance in rectal adenocarcinoma.. *Discover oncology*. PMID: 39276259
3. Diagnostic yield and limitations of whole-genome sequencing for hereditary cerebellar ataxia.. *Brain communications*. PMID: 40488180
4. Molecular Mechanisms and Future Therapeutics for Spinocerebellar Ataxia Type 31 (SCA31).. *Neurotherapeutics : the journal of the American Society for Experimental NeuroTherapeutics*. PMID: 31755042
5. Hypoxia-Induced Adaptations of Embryonic Fibroblasts: Implications for Developmental Processes.. *Biology*. PMID: 39194536

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.8 |
| 高置信度残基 (pLDDT>90) 占比 | 7.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.7% |
| 中等置信 (pLDDT 50-70) 占比 | 51.7% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 20.0% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold低质量预测（pLDDT=58.8），大部分区域无序。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039352; Pfam: 无 |

**染色质调控潜力分析**: 存在 1 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRSF1 | 0.465 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nedd4 | affinity technology | imex:IM-17722|pubmed:11042109|mint:MINT-5213096 |
| PKM | protein kinase assay | imex:IM-22313|pubmed:24606918 |
| EBI-9351778 | protein kinase assay | imex:IM-22313|pubmed:24606918 |
| YAP1 | phage display | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4

**评价**: 互作网络中等：STRING 15 预测 + IntAct 4 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=58.8 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 76.8/100

**核心优势**:
1. BEAN1 -- Protein BEAN1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 1 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. AlphaFold pLDDT 较低（58.8），存在显著无序区
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q3B7T3
- Protein Atlas: https://www.proteinatlas.org/search/BEAN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEAN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3B7T3
- STRING: https://string-db.org/network/9606.BEAN1
- Packet data timestamp: 2026-06-03 03:33:25
