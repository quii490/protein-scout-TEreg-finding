---
type: protein-evaluation
gene: "NUP43"
date: 2026-06-04
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NUP43 — REJECTED (数据不可用)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | NUP43 |
| 数据状态 | 无 harvest packet |
| 评估日期 | 2026-06-04 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 数据不可用 | — | — | — | 无 harvest packet，无法评分 |
| **原始总分** | | | **N/A/180** | |
| **归一化总分** | | | **N/A/100** | |

### 3. 淘汰理由

**数据不可用**: 该基因在 harvest_packets 目录中无对应 JSON 文件，无法进行 /180 标准评分。可能原因包括：
- 该基因未被纳入原始 harvest pipeline
- UniProt 中无对应的人类蛋白条目
- 基因符号命名变化

### 4. 后续建议

- [ ] 确认基因符号是否为新命名（检查 HGNC 最新命名规范）
- [ ] 在 UniProt 检索对应的人类蛋白条目
- [ ] 如找到有效条目，重新运行 harvest pipeline 生成数据包

### 深度机制分析

NUP43（核孔蛋白43 kDa）在已知文献中是核孔复合体（NPC）的Y-complex亚基之一，与NUP85、NUP96、NUP133、NUP160、SEH1和SEC13共同组装成NPC的外环（outer ring）结构——这是核孔复合体对称核心支架的基石。Y-complex采用特征性的Y形模块化架构，其中NUP43与NUP85形成异源二聚体，构成Y-complex的一个臂（stalk），通过beta-propeller折叠和alpha螺线管（alpha-solenoid）重复序列参与coatomer-like的膜弯曲和NPC曲率感应。所有核孔蛋白在翻译后组装过程中均定位于细胞核——核孔复合体横跨核膜，其亚基在核质和胞质两侧均有分布。

NUP43在核孔复合体中的支架功能意味着它间接参与所有核质转运事件——包括转录因子、染色质重塑复合体、RNA结合蛋白以及TE来源mRNA的核输出。核孔复合体的完整性对转座元件沉默至关重要：NPC组分（如NUP93、NUP98）的突变已被证明导致异染色质组织破坏和重复元件去抑制，部分核孔蛋白（如NUP98的FG重复结构域）甚至直接通过与HDAC和Polycomb复合体的物理互作在染色质水平调控转录。

然而，本数据库回收的NUP43条目缺乏harvest packet数据，无法进行/180标准评分。这一数据空白不代表NUP43不重要，而是反映其在本次筛选中未从UniProt/HPA/STRING等公共数据库中获取到足够的结构化注释。考虑到核孔复合体各个亚基在功能上是相互依赖的（亚基缺失通常导致整个Y-complex无法组装），以及NUP43已知的NPC关键结构地位，该蛋白若在后续数据补充后仍值得关注。但就当前数据状态而言，作为TE调控候选靶标缺乏直接的功能基因组学证据支持。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/?query=NUP43
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUP43
- Protein Atlas: https://www.proteinatlas.org/search/NUP43
- AlphaFold: https://alphafold.ebi.ac.uk/search?q=NUP43
